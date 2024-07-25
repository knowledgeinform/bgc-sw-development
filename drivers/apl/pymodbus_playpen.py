import datetime
from enum import Enum
import time
from struct import pack, unpack
from typing import cast

import matplotlib.pyplot as plt
import minimalmodbus
from pymodbus.client import ModbusSerialClient, AsyncModbusSerialClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.pdu import ModbusResponse

# Sample code using https://pymodbus.readthedocs.io/en/latest/index.html
# Still working out recommendations for simulation.


class WatLow:
    def __init__(self, addr: int, baudrate: int) -> None:
        self.address = addr
        self.baudrate = baudrate


watlow_controller = WatLow(1, 9600)


class MinimalModbusDemo:
    """
    Simple direct translation of of existing code to configure and read the temperature using minimalmodbus.

    Note - use of Watlow class should not be hard coded
    """

    def __init__(self) -> None:
        self.instrument = minimalmodbus.Instrument(port="COM7", slaveaddress=watlow_controller.address)
        assert self.instrument.serial is not None
        self.instrument.serial.baudrate = watlow_controller.baudrate

    def writes(self) -> None:
        sen = self.instrument.write_register(388, 95, 0)
        sen = self.instrument.read_register(388)
        assert sen is not None
        # ...

    def read_temperature(self) -> float:
        LowBits = cast(int, self.instrument.read_register(380))
        HighBits = cast(int, self.instrument.read_register(381))
        RawTemp = (HighBits << 16) + LowBits
        s = pack(">L", RawTemp)
        Fahrenheit: float = unpack(">f", s)[0]
        return (Fahrenheit - 32.0) * 5.0 / 9.0


# https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf
# Big Endian
# Registers 16-bit
# 0x6 write_register
# 0x10 write_registers
# would have to supply conversions for long, signed or the like?
# maybe we could write a wrapper to hide all of the cast(ModbusResponse, etc...)


class PyModbusDemo:
    """
    Simple direct translation of of existing minimalmodbus code to configure and read the temperature using pymodbus
    instead.

    Note - use of Watlow class should not be hard coded
    """

    def __init__(self) -> None:
        self.client = ModbusSerialClient(port="COM7", baudrate=watlow_controller.baudrate)
        self.client.connect()
        assert self.client.connected

    def writes(self) -> None:
        sen: ModbusResponse = cast(
            ModbusResponse, self.client.write_register(address=388, value=95, slave=watlow_controller.address)
        )  # code 6
        assert not sen.isError()
        # ...

    def read_temperature(self) -> float:
        # This might be wrong but I think this is it
        read_result = cast(
            ModbusResponse, self.client.read_holding_registers(address=380, count=2, slave=watlow_controller.address)
        )
        assert not read_result.isError()
        decoder = BinaryPayloadDecoder.fromRegisters(
            registers=read_result.registers, byteorder=Endian.BIG, wordorder=Endian.LITTLE
        )
        # Fahrenheit
        Fahrenheit: float = decoder.decode_32bit_float()
        return (Fahrenheit - 32.0) * 5.0 / 9.0

    # doesn't need any synchronization to avoid stomping on the same slave


class ModbusSerialSlave:
    """
    A simple synchronous, typed modbus slave providing support for frequently used functions.

    Instantiated for each slave using the same client.

    Existing pymodbus methods give mypy a fit because they're based on a mixin that works for both
    synchronous and asynchronous clients.

    TODO All asserts should be user or pymodbus exceptions.

    Arguments:
        client -- pymodbus client to wrap
        slave -- slave id of the slave to communicate with
        byteorder -- byte order of each word
        wordorder -- endianness of words when (wordcount  2)
    """

    def __init__(
        self,
        client: ModbusSerialClient,
        slave: int,
        byteorder: Endian = Endian.LITTLE,
        wordorder: Endian = Endian.BIG,
    ) -> None:
        self._client = client
        self._slave = slave
        self._endian = byteorder
        self._wordorder = wordorder

    def read_holding_registers(self, address: int, count: int) -> ModbusResponse:
        result = cast(
            ModbusResponse, self._client.read_holding_registers(address=address, count=count, slave=self._slave)
        )
        assert not result.isError()
        return result

    def read_holding_register_u16(self, address: int) -> int:
        mod_result = self.read_holding_registers(address=address, count=1)
        decoder = BinaryPayloadDecoder.fromRegisters(
            registers=mod_result.registers, byteorder=self._endian, wordorder=self._wordorder
        )
        return cast(int, decoder.decode_16bit_uint())

    def read_holding_register_float(self, address: int) -> float:
        mod_result = self.read_holding_registers(address=address, count=2)
        decoder = BinaryPayloadDecoder.fromRegisters(
            registers=mod_result.registers, byteorder=self._endian, wordorder=self._wordorder
        )
        return cast(float, decoder.decode_32bit_float())

    # ... similarly for other uses such as 16bit s16, float, etc. see AsyncModbusSerialSlave

    def write_register(self, address: int, value: int) -> None:
        mod_result: ModbusResponse = cast(
            ModbusResponse, self._client.write_register(address=address, value=value, slave=self._slave)
        )  # code 6
        assert not mod_result.isError()


class AsyncModbusSerialSlave:
    """
    A simple asynchronous, typed modbus slave providing support for frequently used functions.

    Instantiated for each slave using the same client.

    Synchronization code for client access by multiple clients could be included in this class.

    Existing pymodbus methods give mypy a fit because they're based on a mixin that works for both
    synchronous and asynchronous clients.

    TODO All asserts should be user or pymodbus exceptions.

    Arguments:
        client -- pymodbus client to wrap
        slave -- slave id of the slave to communicate with
        byteorder -- byte order of each word
        wordorder -- endianness of words when (wordcount  2)
    """

    def __init__(
        self,
        client: AsyncModbusSerialClient,
        slave: int,
        byteorder: Endian = Endian.LITTLE,
        wordorder: Endian = Endian.BIG,
    ) -> None:
        self._client = client
        self._slave = slave
        self._endian = byteorder
        self._wordorder = wordorder

    async def read_holding_registers(self, address: int, count: int) -> ModbusResponse:
        result = cast(
            ModbusResponse,
            await self._client.read_holding_registers(address=address, count=count, slave=self._slave),  # type: ignore
        )
        assert not result.isError()
        return result

    async def read_holding_register_u16(self, address: int) -> int:
        mod_result = await self.read_holding_registers(address=address, count=1)
        decoder = BinaryPayloadDecoder.fromRegisters(
            registers=mod_result.registers, byteorder=self._endian, wordorder=self._wordorder
        )
        return cast(int, decoder.decode_16bit_uint())

    async def read_holding_register_s32(self, address: int) -> int:
        mod_result = await self.read_holding_registers(address=address, count=2)
        decoder = BinaryPayloadDecoder.fromRegisters(
            registers=mod_result.registers, byteorder=self._endian, wordorder=self._wordorder
        )
        return cast(int, decoder.decode_32bit_int())

    async def read_holding_register_float(self, address: int) -> float:
        mod_result = await self.read_holding_registers(address=address, count=2)
        decoder = BinaryPayloadDecoder.fromRegisters(
            registers=mod_result.registers, byteorder=self._endian, wordorder=self._wordorder
        )
        return cast(float, decoder.decode_32bit_float())

    # ...

    async def write_register(self, address: int, value: int) -> None:
        mod_result: ModbusResponse = cast(
            ModbusResponse,
            await self._client.write_register(address=388, value=95, slave=self._slave),  # type: ignore
        )  # code 6
        assert not mod_result.isError()


class PyModbusSerialSlaveDemo:
    """
    Simple direct translation of of existing minimalmodbus code to configure and read the temperature using a
    proposed pymodbus slave wrapper class.

    Note - use of Watlow class should not be hard coded
    """

    def __init__(self) -> None:
        self._client = ModbusSerialClient(port="COM7", baudrate=watlow_controller.baudrate)
        self._client.connect()
        assert self._client.connected

        self._slave = ModbusSerialSlave(
            client=self._client,
            slave=watlow_controller.address,
            byteorder=Endian.BIG,
            wordorder=Endian.LITTLE,
        )

    def writes(self) -> None:
        self._slave.write_register(address=388, value=95)

    def read_temperature(self) -> float:
        # This might be wrong but I think this is it
        Fahrenheit = self._slave.read_holding_register_float(address=380)
        return (Fahrenheit - 32.0) * 5.0 / 9.0

    # doesn't need any synchronization to avoid stomping on the same slave


class WhichDemo(Enum):
    MINIMAL_MODBUS = 0
    PYMODBUS_BAREBONES = 1
    PYMODBUS_SERIAL_SLAVE = 2


which_demo = WhichDemo.MINIMAL_MODBUS

modbus: MinimalModbusDemo | PyModbusDemo | PyModbusSerialSlaveDemo

if which_demo == WhichDemo.MINIMAL_MODBUS:
    modbus = MinimalModbusDemo()
elif which_demo == WhichDemo.PYMODBUS_BAREBONES:
    modbus = PyModbusDemo()
elif which_demo == WhichDemo.PYMODBUS_SERIAL_SLAVE:
    modbus = PyModbusSerialSlaveDemo()
else:
    raise ValueError(f"Unsupported which_demo({which_demo})")

modbus.writes()
x = []
y = []


while True:
    CurrentTime = datetime.datetime.now()

    Celsius = modbus.read_temperature()

    print(str(CurrentTime) + " -- " + str(float(Celsius)))

    # plotting Temp vs Time
    y.append(Celsius)
    x.append(CurrentTime)

    plt.clf()
    plt.scatter(x, y)  # type: ignore
    plt.xlabel("Time")
    plt.ylabel("Analog Input 1 Temperature")
    plt.plot(x, y)  # type: ignore
    plt.pause(0.5)
    plt.clf()
    plt.draw()

    time.sleep(1)
