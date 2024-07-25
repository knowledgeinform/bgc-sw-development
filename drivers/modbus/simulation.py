import asyncio
from typing import Callable, Dict, Final, Tuple, Type, TypeAlias, Union, cast

from pymodbus.constants import Endian

from drivers.modbus.base_classes import AsyncModbusBase, AsyncModbusSlaveBase, ModbusBase

"""
Modbus simulation supporting the following:
* Typed reads/writes
* Reads write and return default value for type if not written
* Once written values must retain their type
* Reads / Writes can be overridden independent callback for every address
"""
# Values supported under simulation
Value: TypeAlias = Union[int, float]
SIMULATED_TYPES: Final[Tuple[Type, ...]] = (int, float)

ModbusAddress: TypeAlias = int

# Map [address] -> simulated value
SimulatedValues: TypeAlias = Dict[ModbusAddress, Value]

# Callbacks for Read / Write.  Each receives all simulated values so global state changes can be simulated
SimulatedReadFun: TypeAlias = Callable[[SimulatedValues, ModbusAddress], Value]
SimulatedWriteFun: TypeAlias = Callable[[SimulatedValues, ModbusAddress, Value], None]


def default_simulated_read_fun(values: SimulatedValues, address: ModbusAddress) -> Value:
    """
    Basic function to read a value from simulated modbus registers

    Arguments:
        values -- simulated values to read from
        address -- address to read from

    Returns:
        values[address]
    """
    return values[address]


def default_simulated_write_fun(values: SimulatedValues, address: ModbusAddress, value: Value) -> None:
    """
    Basic function to write a value from simulated modbus registers

    Arguments:
        values -- values to write to
        address -- address to write to
        value -- value to write
    """
    if address in values:
        current_type = type(values[address])
        assert isinstance(
            value, current_type
        ), f"default_simulated_write_fun({address}, {value}) attempt to change existing type from {current_type} to {type(value)}"
    values[address] = value


class SimulatedRegisters:
    def __init__(self) -> None:
        self._values: SimulatedValues = {}
        self._read_fs: Dict[ModbusAddress, SimulatedReadFun] = {}
        self._write_fs: Dict[ModbusAddress, SimulatedWriteFun] = {}

    def _default_read(self, index: ModbusAddress) -> Value:
        return self._values[index]

    def _read_holding_register_value(self, address: int, type_as: Type) -> Value:
        assert address >= 0, f"Attempt to access negative address: {address}"

        if address not in self._values:
            default_value = type_as()
            self._values[address] = default_value

        if address not in self._read_fs:
            self._read_fs[address] = default_simulated_read_fun

        result = self._read_fs[address](self._values, address)
        assert isinstance(result, type_as), f"Read({address}, {type_as}) type mismatch, current type is {type(result)})"
        assert isinstance(
            result, SIMULATED_TYPES
        ), f"Read({address}, {type_as}), type must be one of ({', '.join(map(str, SIMULATED_TYPES))})"

        # mypy loses the ball on SIMULATED_TYPES above
        return result  # type: ignore

    def _write_holding_register_value(self, address: int, value: Value) -> None:
        assert address >= 0, f"Attempt to access negative address: {address}"
        assert isinstance(
            value, SIMULATED_TYPES
        ), f"Write({address}, {value}), type must be one of ({', '.join(map(str, SIMULATED_TYPES))})"

        if address not in self._write_fs:
            self._write_fs[address] = default_simulated_write_fun

        self._write_fs[address](self._values, address, value)

    def set_values(self, *values: Tuple[ModbusAddress, Value]) -> None:
        for address, value in values:
            self._write_holding_register_value(address, value)

    def set_write_fs(self, *write_fs: Tuple[ModbusAddress, SimulatedWriteFun]) -> None:
        for address, write_f in write_fs:
            self._write_fs[address] = write_f

    def set_read_fs(self, *read_fs: Tuple[ModbusAddress, SimulatedReadFun]) -> None:
        for address, read_f in read_fs:
            self._read_fs[address] = read_f

    def set_read_write_fs(self, *read_write_fs: Tuple[ModbusAddress, SimulatedReadFun, SimulatedWriteFun]) -> None:
        for address, read_f, write_f in read_write_fs:
            self._read_fs[address] = read_f
            self._write_fs[address] = write_f


class SimulatedModbus(ModbusBase, SimulatedRegisters):
    def __init__(self, byteorder: Endian, wordorder: Endian) -> None:
        ModbusBase.__init__(self, byteorder=byteorder, wordorder=wordorder)
        SimulatedRegisters.__init__(self)

    def read_holding_register_float(self, address: int) -> float:
        return cast(float, self._read_holding_register_value(address, float))

    def read_holding_register_u16(self, address: int) -> int:
        return cast(int, self._read_holding_register_value(address, int))

    def write_register_float(self, address: int, value: float) -> None:
        self._write_holding_register_value(address, value)

    def write_register_u16(self, address: int, value: int) -> None:
        self._write_holding_register_value(address, value)

    # populate


class AsyncSimulatedModbus(AsyncModbusBase, SimulatedRegisters):
    def __init__(self, byteorder: Endian, wordorder: Endian) -> None:
        AsyncModbusBase.__init__(self, byteorder=byteorder, wordorder=wordorder)
        SimulatedRegisters.__init__(
            self,
        )

    async def read_holding_register_float(self, address: int) -> float:
        return cast(float, self._read_holding_register_value(address=address, type_as=float))

    async def read_holding_register_u16(self, address: int) -> int:
        return cast(int, self._read_holding_register_value(address=address, type_as=int))

    async def write_register_float(self, address: int, value: float) -> None:
        self._write_holding_register_value(address, value)

    async def write_register_u16(self, address: int, value: int) -> None:
        self._write_holding_register_value(address, value)


class SimulatedModbusSlave(SimulatedModbus):
    def __init__(self, slave: int, byteorder: Endian, wordorder: Endian) -> None:
        SimulatedModbus.__init__(self, byteorder=byteorder, wordorder=wordorder)


class AsyncSimulatedModbusSlave(AsyncModbusSlaveBase, AsyncSimulatedModbus):
    def __init__(self, slave: int, byteorder: Endian, wordorder: Endian) -> None:
        AsyncSimulatedModbus.__init__(self, byteorder=byteorder, wordorder=wordorder)
        AsyncModbusSlaveBase.__init__(self, slave=slave, byteorder=byteorder, wordorder=wordorder)


async def async_main() -> None:
    uut = AsyncSimulatedModbusSlave(slave=2, byteorder=Endian.LITTLE, wordorder=Endian.BIG)

    # from pymodbus.client import ModbusSerialClient

    # client = ModbusSerialClient("COM7", baudrate=9600)
    # y = ModbusSerialSlave(client=client, slave=2, byteorder=Endian.LITTLE, wordorder=Endian.BIG)

    x = uut.read_holding_register_float(18)
    assert isinstance(x, float) and x == 0.0
    y = uut.read_holding_register_u16(2019)
    assert isinstance(y, int) and y == 0

    await uut.write_register_float(27, 19.3)
    assert 19.29 < await uut.read_holding_register_float(27) < 19.31
    assert uut.read_holding_register_float(18) == 0.0

    await uut.write_register_u16(19, 73)
    assert uut.read_holding_register_u16(19) == 73
    assert uut.read_holding_register_u16(2019) == 0

    try:  # to write as wrong type
        await uut.write_register_float(19, 73.0)
        assert False
    except Exception as _:
        pass

    try:  # to read as wrong type
        await uut.read_holding_register_float(19)
        assert False
    except Exception as _:
        pass

    try:  # to read bad address
        await uut.read_holding_register_u16(-1)
        assert False
    except Exception as _:
        pass

    try:  # to write bad address
        await uut.write_register_u16(-1, 28)
        assert False
    except Exception as _:
        pass


if __name__ == "main":
    asyncio.run(async_main())
