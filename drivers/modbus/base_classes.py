from abc import ABC, abstractmethod
from typing import Any
from pymodbus.constants import Endian
from pymodbus.pdu import ModbusResponse


class ModbusSlaveException(Exception):
    """
    Exception resulting from using the modbus

    Arguments:
        response - the response error returned by the underlying driver
    """

    def __init__(self, response: ModbusResponse, *args: Any) -> None:
        super().__init__(*args)
        self.response = response


class ModbusBase(ABC):
    """
    Abstract base class for a basic typed synchronous modbus interface.

    TODO document
    Arguments:
        byteorder -- _description_
        wordorder -- _description_
    """

    def __init__(self, byteorder: Endian, wordorder: Endian) -> None:
        self._byteorder = byteorder
        self._wordorder = wordorder

    @abstractmethod
    def read_holding_register_float(self, address: int) -> float:
        pass

    @abstractmethod
    def read_holding_register_u16(self, address: int) -> int:
        pass

    @abstractmethod
    def write_register_float(self, address: int, value: float) -> None:
        pass

    @abstractmethod
    def write_register_u16(self, address: int, value: int) -> None:
        pass

    @property
    def byteorder(self) -> Endian:
        return self._byteorder

    @property
    def wordorder(self) -> Endian:
        return self.wordorder


class AsyncModbusBase(ABC):
    def __init__(self, byteorder: Endian, wordorder: Endian) -> None:
        """
        Abstract base class for a basic typed asynchronous modbus interface.

        TODO document
        Arguments:
            byteorder -- _description_
            wordorder -- _description_
        """
        self._byteorder = byteorder
        self._wordorder = wordorder

    @abstractmethod
    async def read_holding_register_float(self, address: int) -> float:
        pass

    @abstractmethod
    async def read_holding_register_u16(self, address: int) -> int:
        pass

    @abstractmethod
    async def write_register_float(self, address: int, value: float) -> None:
        pass

    @abstractmethod
    async def write_register_u16(self, address: int, value: int) -> None:
        pass

    @property
    def byteorder(self) -> Endian:
        return self._byteorder

    @property
    def wordorder(self) -> Endian:
        return self._wordorder


class ModbusSlaveBase(ModbusBase):
    """
    Abstract base class for a basic typed asynchronous modbus slave interface.

    TODO document
    Arguments:
        slave -- _description_
        byteorder -- _description_
        wordorder -- _description_
    """

    def __init__(self, slave: int, byteorder: Endian, wordorder: Endian) -> None:
        ModbusBase.__init__(self, byteorder=byteorder, wordorder=wordorder)
        self._slave = slave

    @property
    def slave(self) -> int:
        return self._slave


class AsyncModbusSlaveBase(AsyncModbusBase):
    """
    Abstract base class for a basic typed synchronous modbus slave interface.

    TODO document
    Arguments:
        slave -- _description_
        byteorder -- _description_
        wordorder -- _description_
    """

    def __init__(self, slave: int, byteorder: Endian, wordorder: Endian) -> None:
        self._slave = slave
        AsyncModbusBase.__init__(self, byteorder=byteorder, wordorder=wordorder)

    @property
    def slave(self) -> int:
        return self._slave
