from dataclasses import dataclass
from typing import Literal, Tuple, TypeAlias, Union

"""
Class that implements communication protocol for Alicat Basis mass flow controller (mfc).

See https://gitlab.jhuapl.edu/qai/ltpms/mms-sw.git code/software/applications/aerosol/alicat/src/AlicatDriver.* for
more information.
"""

TbdSerialPort: TypeAlias = int

# FIXME probably should use exceptions instead of False | Result


class AlicatBasisMfcDriver:
    """
    Preparing to use the driver should be a two step process:
        Construct the object
        Call PrepareToUseSlpm(), optionally enable logging prior to this desired
    """

    @dataclass
    class DeviceParams:
        """Alicat parameters read from the board"""

        unit_id: str
        temperature: str
        tempUnits: str
        massFlowSlpm: str
        massFlowUnits: str  # SLPM[(native)]
        flowSetpointSlpm: float
        setpointUnits: str  # SLPM[(native)]
        gasType: str

    def __init__(self, id: str, serial_port: TbdSerialPort) -> None:
        if not self.is_valid_id(id):
            raise ValueError(f"{self.__class__.__name__}({id}), id must be A..Z")
        assert self.is_valid_id(id), "Id must be"
        self._id = id
        self._serial_port = serial_port
        self._full_scale_slpm_flow: float = 0
        self._logging_enabled: bool = False
        self._slpm_flow_units: str = "SLPM(UNKNOWN)"
        self._slpm_per_device_flow_unit: float = 0.0  # for SLPM -> fractional effort conversions
        # ...

    def prepare_to_use_slpm(self) -> float:
        """
        Prepare the driver to use SLPM units.
        Until called it's assumed the MFC has a range of 0 SLPM and
        conversions to SLPM will yield 0.

        Returns:
            max SLPM flow rate, 0 if there is an error
        """
        return 0.0

    @classmethod
    def is_valid_id(cls, id: str) -> bool:
        """
        Determine if id is a valid Alicat id character
        """
        return (len(id) == 1) and (id[0].isupper() or (id[0] == "*"))

    # TBD include fractional methods as needed

    async def set_flow_setpoint_slpm(self, slpm: float) -> bool:
        """
        Set the flow setpoint in SLPM units.  Units and range are configured
        by the manufacturer, see GetFullScaleRange().
        Full scale range defaults to 0 until PrepareToUseSlpm() is used.

        Return: >=0 successful, failure otherwise

        Arguments:
            slpm -- flowRate, si units, 0..full scale range, capped at full scale

        Returns:
            successful
        """
        return True

    def set_id(self, id: str) -> bool:
        return True

    async def get_status(self) -> Union[Literal[False], DeviceParams]:
        return False

    async def get_full_scale_range(self) -> Union[Literal[False], Tuple[float, str]]:
        """
        Get the full scale range of the unit in device units.

        Returns:
            False | (full scale range in device units, device units reported by the device)
        """
        return (5, "SCCM")

    @property
    def slpm_flow_range(self) -> Tuple[float, float]:
        """
        Return the (min SLPM flow, max SLPM flow) for the unit.
        """
        return (0.0, self._full_scale_slpm_flow)

    # TBD include logging control and exclusive access as needed
