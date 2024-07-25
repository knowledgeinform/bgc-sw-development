from enum import Enum, unique
from typing import Any, Final, Type

from pymodbus.constants import Endian

# Register definitions, types and driver or the Watlow EZ Zone RMH as defined in
# "Bronkhorst 917045-Manual-IQ-FLOW.pdf"
# Available at "Box\Ballistic GC\2023 BGC Redesign\Component exchange\Mass flow\"


# TODO move to more general apl
class ModbusFixedString:
    def __init__(self, length: int) -> None:
        self.length = length

    def regs_to_string(self, x: Any) -> str:
        # TODO verify #regs
        raise NotImplementedError(f"{self.__class__.__name__}.{self.regs_to_string.__name__} not implemented")

    def str_to_regs(self, x: str) -> Any:
        # TODO trim / pad string
        raise NotImplementedError(f"{self.__class__.__name__}.{self.regs_to_string.__name__} not implemented")


@unique
class Register(Enum):
    """
    Bronkhorst register definitions from the specification identified above
    """

    def __init__(self, address: int, offset: int, type_: Type, access: str) -> None:
        """
        Define a Bronkhorst Register.

        Arguments:
            address -- Modbus relative address
            offset -- offset between corresponding registers for indexed registers, 0 = register not indexed
            type_ -- Type the register stores
            access -- combination of 'R'ead / 'W'rite / 'L'ocked

        NOTE: Locked regs can only be written when the 'Init Reset' parameter is set to 64.
        """
        self.address = address
        self.offset = offset
        self.type = type_
        self.access = access

        # some sanity checks for ranges / types, type checkers fall short, e.g. X = 4 would only error at runtime
        assert address > 0
        assert (offset >= 0) and ((offset % 10) == 0)
        assert issubclass(type_, (int, float))  # includes IntEnum
        assert all(map(lambda s: s in "RWL", access)) and ("R" in access)

    def register_name(self) -> str:
        """
        Enum name split into words with leading caps.
        """
        words = self.name.lower().split("_")
        return " ".join(map(lambda s: s[0].upper() + s[1:], words))

    # Basic measurement and control parameters
    MEASURED_VALUE = (0x0020, 0, int, "R")  # [0, 41942], 32000 = 100%
    SETPONT = (0x0021, 0, int, "RW")  # [0, 32000]

    # Basic Identification
    USER_TAG = (0xF130, 0, ModbusFixedString(16), "RW")
    CUSTOMER_MODEL = (0xF120, ModbusFixedString(16), "RWL")
    SERIAL_NUMBER = (0xF118, ModbusFixedString(20), "R")
    BHT_MODEL_NUMBER = (0xF110, ModbusFixedString(23), "R")


class BronkhorstIqFlowMfcDriver:
    # TBD not specified by manufacturer
    BYTE_ORDER: Final[Endian] = Endian.BIG
    WORD_ORDER: Final[Endian] = Endian.LITTLE

    pass
