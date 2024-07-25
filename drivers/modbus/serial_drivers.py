from typing import Awaitable, List, cast

from pymodbus.client import AsyncModbusSerialClient, ModbusSerialClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.pdu import ModbusResponse

from drivers.modbus.base_classes import AsyncModbusSlaveBase, ModbusSlaveException, ModbusSlaveBase

# Sample code using https://pymodbus.readthedocs.io/en/latest/index.html
# Still working out recommendations for simulation.

# MAP : Modbus Application Protocol
# Pymodbus implements MAP: https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf
# Per the MAP we have the following:
#   Registers 16-bit
#   Ues a bit-endian representation for numerical addresses and data items
#   0x6 write_register
#   0x10 write_registers


class ModbusSerialSlave(ModbusSlaveBase):
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
        ModbusSlaveBase.__init__(self, slave=slave, byteorder=byteorder, wordorder=wordorder)

        # TODO switch over to use properties
        self._client = client
        self._builder = BinaryPayloadBuilder(byteorder=byteorder, wordorder=wordorder)

    def read_holding_registers(self, address: int, count: int) -> ModbusResponse:
        result = cast(
            ModbusResponse, self._client.read_holding_registers(address=address, count=count, slave=self.slave)
        )
        if not result.isError():
            return result
        raise ModbusSlaveException(result)

    def write_register(self, address: int, value: int) -> None:
        mb_result = cast(ModbusResponse, self._client.write_register(address=address, value=value, slave=self.slave))
        if mb_result.isError():
            raise ModbusSlaveException(mb_result)

    def write_registers(self, address: int, values: List[int]) -> None:
        mb_result = cast(ModbusResponse, self._client.write_registers(address=address, values=values, slave=self.slave))
        if mb_result.isError():
            raise ModbusSlaveException(mb_result)

    def read_holding_register_float(self, address: int) -> float:
        mb_result = self.read_holding_registers(address=address, count=2)
        decoder = BinaryPayloadDecoder.fromRegisters(
            registers=mb_result.registers, byteorder=self.byteorder, wordorder=self.wordorder
        )
        return cast(float, decoder.decode_32bit_float())

    def read_holding_register_u16(self, address: int) -> int:
        mb_result = self.read_holding_registers(address=address, count=1)
        decoder = BinaryPayloadDecoder.fromRegisters(
            registers=mb_result.registers, byteorder=self.byteorder, wordorder=self.wordorder
        )
        return cast(int, decoder.decode_16bit_uint())

    def write_register_float(self, address: int, value: float) -> None:
        self._builder.reset()
        self._builder.add_32bit_float(value=value)
        self.write_registers(address=address, values=self._builder.to_registers())

    def write_register_u16(self, address: int, value: int) -> None:
        self._builder.reset()
        self._builder.add_16bit_uint(value=value)
        self.write_register(address=address, value=self._builder.to_registers()[0])


class AsyncModbusSerialSlave(AsyncModbusSlaveBase):
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
        AsyncModbusSlaveBase.__init__(self, slave=slave, byteorder=byteorder, wordorder=wordorder)
        self._client = client
        self._builder = BinaryPayloadBuilder(byteorder=byteorder, wordorder=wordorder)

    async def read_holding_registers(self, address: int, count: int) -> ModbusResponse:
        mb_result = await cast(
            Awaitable[ModbusResponse],
            self._client.read_holding_registers(address=address, count=count, slave=self.slave),
        )
        if not mb_result.isError():
            return mb_result
        raise ModbusSlaveException(mb_result)

    async def write_register(self, address: int, value: int) -> None:
        mb_result = await cast(
            Awaitable[ModbusResponse],
            self._client.write_register(address=address, value=value, slave=self.slave),
        )
        if mb_result.isError():
            raise ModbusSlaveException(mb_result)

    async def write_registers(self, address: int, values: List[int]) -> None:
        mb_result = await cast(
            Awaitable[ModbusResponse],
            self._client.write_registers(address=address, values=values, slave=self.slave),
        )
        if mb_result.isError():
            raise ModbusSlaveException(mb_result)

    async def read_holding_register_float(self, address: int) -> float:
        mod_result = await self.read_holding_registers(address=address, count=2)
        decoder = BinaryPayloadDecoder.fromRegisters(
            registers=mod_result.registers, byteorder=self.byteorder, wordorder=self.wordorder
        )
        return cast(float, decoder.decode_32bit_float())

    async def read_holding_register_u16(self, address: int) -> int:
        mod_result = await self.read_holding_registers(address=address, count=1)
        decoder = BinaryPayloadDecoder.fromRegisters(
            registers=mod_result.registers, byteorder=self.byteorder, wordorder=self.wordorder
        )
        return cast(int, decoder.decode_16bit_uint())

    async def write_register_float(self, address: int, value: float) -> None:
        self._builder.reset()
        self._builder.add_32bit_float(value=value)
        await self.write_registers(address=address, values=self._builder.to_registers())

    async def write_register_u16(self, address: int, value: int) -> None:
        self._builder.reset()
        self._builder.add_16bit_uint(value=value)
        await self.write_register(address=address, value=self._builder.to_registers()[0])
