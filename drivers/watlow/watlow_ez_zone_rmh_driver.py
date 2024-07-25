from __future__ import annotations

import asyncio
from enum import Enum, IntEnum, unique
from typing import Any, Dict, Final, Type, Union

from pymodbus.constants import Endian

from drivers.modbus.base_classes import AsyncModbusSlaveBase
from drivers.modbus.serial_drivers import AsyncModbusSerialClient, AsyncModbusSerialSlave
from drivers.modbus.simulation import AsyncSimulatedModbusSlave


# Register definitions, types and driver or the Watlow EZ Zone RMH as defined in "RMH user manual Rev F.pdf"
# Available at "Box\Ballistic GC\2023 BGC Redesign\Component exchange\Temperature control"
@unique
class SensorType(IntEnum):
    OFF = 62
    THERMOCOUPLE = 95
    MILLIVOLTS = 56
    VOLTS_DC = 104
    MILLIAMPS_DC = 112
    RTD_100_OHM = 113
    RTD_1000_OHM = 114
    POTENTIOMETER_1K_OHM = 155
    THERMISTOR = 229


@unique
class SourceFunctionA(IntEnum):
    NONE = 61
    ANALOG_INPUT = 142
    LINEARIZATION = 238
    MATH = 240
    PROCESS_VALUE = 241
    VARIABLE = 245


@unique
class TcLinearization(IntEnum):
    B = 11
    C = 15
    D = 23
    E = 26
    F = 30
    J = 4
    K = 48
    N = 58
    R = 80
    S = 84
    T = 93


@unique
class Units(IntEnum):
    ABSOLUTE_TEMPERATURE = 1540
    RELATIVE_HUMIDITY = 1538
    PROCESS = 75
    POWER = 73


@unique
class DisplayPrecision(IntEnum):
    WHOLE = 105
    TENTHS = 94
    HUNDREDTHS = 40
    THOUSANDTHS = 96


class HeatAlgorithm(IntEnum):
    OFF = 62
    PID = 71
    ON_OFF = 64


@unique
class Register(Enum):
    """
    Watlow register definitions from the specification identified above
    """

    def __init__(self, address: int, offset: int, type_: Type, access: str) -> None:
        """
        Define a Watlow Register.

        Arguments:
            address -- Modbus relative address
            offset -- offset between corresponding registers for indexed registers, 0 = register not indexed
            type_ -- Type the register stores
            access -- combination of 'R'ead / 'W'rite / 'E'eprom / user 'S'et
        """
        self.address = address
        self.offset = offset
        self.type = type_
        self.access = access

        # some sanity checks for ranges / types, type checkers fall short, e.g. X = 4 would only error at runtime
        assert address > 0
        assert (offset >= 0) and ((offset % 10) == 0)
        assert issubclass(type_, (int, float))  # includes IntEnum
        assert all(map(lambda s: s in "RWES", access)) and ("R" in access)

    @property
    def register_name(self) -> str:
        """
        Enum name split into words with leading caps.
        """
        words = self.name.lower().split("_")
        return " ".join(map(lambda s: s[0].upper() + s[1:], words))

    # NOTE: Watlow has menus for some related features broken into Operations / Setup pages, e.g. Analog Input

    # Analog Input Menu
    ANALOG_INPUT_VALUE = (380, 90, float, "R")
    ANALOG_INPUT_ERROR = (382, 90, int, "R")  # TODO AnalogInputError
    SENSOR_TYPE = (388, 90, SensorType, "RWES")
    TC_LINEARIZATION = (390, 90, TcLinearization, "RWES")
    UNITS = (462, 90, Units, "RWES")
    SCALE_LOW = (408, 90, float, "RWES")
    CALIBRATION_OFFSET = (402, 90, float, "RWES")
    # ...
    # Process Value Menu
    PROCESS_FUNCTION = (8260, 70, int, "RWES")  # TODO ProcessFunction
    # ...
    # Digital Input/Output Menu
    IO_DIRECTION = (1820, 30, int, "RWES")  # TODO IoDirection
    OUTPUT_FUNCTION = (1828, 30, int, "RWES")  # IoFunction, OutputFunction
    OUTPUT_FUNCTION_INSTANCE = (1830, 30, int, "RWES")  # [1,250]
    OUTPUT_SOURCE_ZONE = (1842, 30, int, "RWES")  # [0,24]
    OUTPUT_TIME_BASE_TYPE = (1822, 30, int, "RWES")  # IoFixedTimeBase
    OUTPUT_FIXED_TIME_BASE = (1824, 30, float, "RWES")  # [0.1, 60.0]
    OUTPUT_LOW_POWER_SCALE = (1836, 30, float, "RWES")  # [ 0.0, 100.0]
    OUTPUT_HIGH_POWER_SCALE = (1838, 30, float, "RWES")  # [0.0, 100.0]
    # ...
    # Action Menu
    ACTION_FUNCTION = (2184, 20, int, "RWES")  # TODO ActionFunction
    # ...
    # Control Loop Menu
    # ...
    CONTROL_SOURCE_FUNCTION_A = (4156, 70, SourceFunctionA, "RWE")
    # Output Menu
    # See Digital Input Output Menu
    OUTPUT_PROCESS_TYPE = (16540, 60, int, "RWES")  # TODO OutputProcessType
    # ...
    # Alarm Menu
    ALARM_TYPE = (2688, 60, int, "RWES")  # TODO AlarmType
    # ...
    # Linearization Menu
    LINEARIZATION_FUNCTION = (14388, 70, int, "RWES")  # TODO LinearizationFunction
    # ...
    # Compare Menu
    COMPARE_FUNCTION = (11276, 40, int, "RWES")  # TODO CompareFunction
    # ...
    # Timer Menu
    TIMER_FUNCTION = (13196, 50, int, "RWES")  # TODO TimerFunction
    # ...
    # Counter Menu
    COUNTER_FUNCTION = (12236, 40, int, "RWES")  # TODO CounterFunction
    # ...
    # Logic Menu
    LOGIC_FUNCTION = (9404, 80, int, "RWES")  # TODO LogicFunction
    # ...
    # Math Menu
    MATH_FUNCTION = (6580, 70, int, "RWES")  # TODO MathFunction
    # ...
    #
    VARIABLE_DATA_TYPE = (16060, 20, int, "RWES")  # TODO VariableDataType
    # ...
    # Global Menu
    DISPLAY_UNITS = (368, 0, int, "RWES")  # TODO GlobalDisplayUnits
    # ...
    # Communications Menu
    BAUD = (6504, 0, int, "RWE")  # TODO BaudRate
    # ...


_address_to_register_map: Dict[int, Register] = {r.address: r for r in Register}


class AsyncWatlowEzZoneRmhDriver:
    # per Chapter 2 Modbus RTU Protocol
    BYTE_ORDER: Final[Endian] = Endian.BIG
    WORD_ORDER: Final[Endian] = Endian.LITTLE

    def __init__(
        self,
        slave: AsyncModbusSlaveBase,
    ) -> None:
        # TODO document
        self._slave = slave

    @staticmethod
    def index_offset(base: int, offset: int, index: int) -> int:
        return base + (offset * index)

    async def write_any_register(self, register: Union[Register, int], index: int, value: Any) -> None:
        """
        Method to write to any register we have data for.
        Recommend we use the normal named methods for specifically implemented registers.
        This method is really just for general access to most anything
        """
        if isinstance(register, int):
            register = _address_to_register_map[register]

        reg_str = f"{register.register_name}({register.value})"

        assert "W" in register.access, f"{reg_str}, attempt to write to read only register"

        assert index >= 0
        if index > 0:
            assert register.offset == 0, f"{reg_str}, attempt to access [{index}] of unindexed register"
        else:
            index = 0

        offset = register.offset if register.offset is not None else 0

        address_ = register.address + (index * offset)

        assert isinstance(value, register.type), f"Writing {type(value)} to {reg_str} expected {register.type}"

        if isinstance(value, int):
            await self._slave.write_register_u16(address=address_, value=int(value))
        elif isinstance(value, float):
            await self._slave.write_register_float(address=address_, value=value)
        else:
            raise ValueError(f"{reg_str}, attempt to write {type(value)}, unknown type")

    async def read_any_register(self, register: Union[Register, int], index: int) -> Any:
        """
        Method to read from any register we have data for.
        Recommend we use the normal named methods for specifically implemented registers.
        This method is really just for general access to most anything
        """
        if isinstance(register, int):
            register = _address_to_register_map[register]

        reg_str = f"{register.register_name}({register.value})"

        assert "W" in register.access, f"{reg_str}, attempt to read from unreadable"

        assert index >= 0
        if index > 0:
            assert register.offset == 0, f"{reg_str}, attempt to access [{index}] of unindexed register"
        else:
            index = 0

        offset = register.offset if register.offset is not None else 0

        address_ = register.address + (index * offset)

        if issubclass(register.type, int):
            result = await self._slave.read_holding_register_u16(address=address_)
            return register.type(result) if issubclass(register.type, IntEnum) else result
        elif issubclass(register.type, float):
            return await self._slave.read_holding_register_float(address=address_)
        else:
            raise ValueError(f"{reg_str}, attempt to read {register.type} unknown type")

    ############################
    # Analog Input Menu
    ############################

    async def read_analog_input_value(self, analog_input: int) -> float:
        return await self._slave.read_holding_register_float(
            address=self.index_offset(
                base=Register.ANALOG_INPUT_VALUE.address,
                offset=Register.ANALOG_INPUT_VALUE.offset,
                index=analog_input,
            )
        )

    ############################
    # Global Menu
    ############################

    # ...


async def run_test(
    slave: AsyncModbusSlaveBase,
    float_register: Register,
    int_register: Register,
) -> None:
    # create the driver
    watlow = AsyncWatlowEzZoneRmhDriver(slave=slave)

    ###############################################
    # try to tweek an innocuous float register
    innocuous_register = float_register
    assert innocuous_register.type == float  # otherwise we need to change values below

    # read the current value
    old_value = await watlow.read_any_register(innocuous_register, 0)
    assert isinstance(old_value, innocuous_register.type)

    # tweek it
    tweeked_value = old_value + 0.1
    await watlow.write_any_register(innocuous_register, 0, value=tweeked_value)

    # read it back and verify the change , inexact comparison for floating point
    new_value = await watlow.read_any_register(innocuous_register, 0)
    assert (tweeked_value - 0.001) < new_value < (tweeked_value + 0.001)

    # put back the old value
    await watlow.write_any_register(innocuous_register, 0, value=old_value)
    new_value = await watlow.read_any_register(innocuous_register, 0)
    assert (old_value - 0.001) < new_value < (old_value + 0.001)

    ###############################################
    # try to tweek an innocuous int register
    innocuous_register = int_register
    assert innocuous_register.type == int  # otherwise we need to change values below

    # read the current value
    old_value = await watlow.read_any_register(innocuous_register, 0)
    assert isinstance(old_value, innocuous_register.type)

    # tweek it
    tweeked_value = 1367  # Average
    await watlow.write_any_register(innocuous_register, 0, value=tweeked_value)

    # read it back and verify the change , inexact comparison for floating point
    new_value = await watlow.read_any_register(innocuous_register, 0)
    assert new_value == 1367

    # put back the old value
    await watlow.write_any_register(innocuous_register, 0, value=old_value)
    new_value = await watlow.read_any_register(innocuous_register, 0)
    assert new_value == old_value


if __name__ == "__main__":

    async def run_on_hw(
        slave_id: int,
        float_register: Register,
        int_register: Register,
    ) -> None:
        # establish connection...
        client = AsyncModbusSerialClient("COM7", baudrate=38400)
        await client.connect()

        try:
            assert client.connected
            slave = AsyncModbusSerialSlave(
                client,
                slave=slave_id,
                byteorder=AsyncWatlowEzZoneRmhDriver.BYTE_ORDER,
                wordorder=AsyncWatlowEzZoneRmhDriver.WORD_ORDER,
            )
            await run_test(slave=slave, float_register=float_register, int_register=int_register)
        finally:
            client.close()

    async def test_on_simulated_hw(
        slave_id: int,
        float_register: Register,
        int_register: Register,
    ) -> None:
        slave = AsyncSimulatedModbusSlave(
            slave=slave_id,
            byteorder=AsyncWatlowEzZoneRmhDriver.BYTE_ORDER,
            wordorder=AsyncWatlowEzZoneRmhDriver.WORD_ORDER,
        )
        await run_test(slave=slave, float_register=float_register, int_register=int_register)

    test_on_hw = True
    slave_id = 1
    innoccuous_float_register = Register.CALIBRATION_OFFSET
    innocuous_int_register = Register.MATH_FUNCTION

    # simple innocuous test program
    if test_on_hw:
        asyncio.run(
            run_on_hw(
                slave_id=slave_id,
                float_register=innoccuous_float_register,
                int_register=innocuous_int_register,
            )
        )
    else:
        asyncio.run(
            test_on_simulated_hw(
                slave_id=slave_id,
                float_register=innoccuous_float_register,
                int_register=innocuous_int_register,
            )
        )
