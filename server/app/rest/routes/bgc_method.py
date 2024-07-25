from typing import List
from enum import Enum
from typing import Annotated, TypeAlias
from fastapi import APIRouter
from pydantic import BaseModel, Field, ValidationInfo, field_validator
from server.app.core.device_info import IsocraticFlowName
from server.app.core.device_info import IsocraticTemperatureName
from server.app.rest.utils.types import IsocraticFlowPair, IsocraticTemperaturePair

from server.utils.type_utils import unique

router = APIRouter()


# Probably belongs elsewhere... for access by utils that run the method
class BgcMethodTypeNames(Enum):
    CALIBRATION = "calibration"
    SCAN = "scan"


Flows: TypeAlias = List[IsocraticFlowPair]
Temperatures: TypeAlias = List[IsocraticTemperaturePair]


# Probably belongs elsewhere... for access by utils that run the method
class BgcMethod(BaseModel):
    type: BgcMethodTypeNames
    name: Annotated[str, "Name to show the user"]
    temperatures: Temperatures = Field(description="Overridden isocratic temperatures.")
    flows: Flows = Field(description="Overridden isocratic flows.")
    clarity_name: Annotated[str, "Name to find the clarity method"]

    # similar possible for temperatures
    # see https://docs.pydantic.dev/2.5/concepts/validators/
    @field_validator("flows")
    @classmethod
    def flow_names_must_be_unique(cls, v: Flows, info: ValidationInfo) -> Flows:
        if not unique([x.name for x in v]):
            raise ValueError("names must be unique")
        return v


class BgcMethodRestType(Enum):
    CALIBRATION = BgcMethodTypeNames.CALIBRATION.value
    SCAN = BgcMethodTypeNames.SCAN.value
    ALL = "all"


@router.get(
    path="/get-methods/{type}",
    name="get",
    description="Get all BGC methods of a given type",
)
async def get_bgc_methods(type: BgcMethodRestType) -> List[BgcMethod]:
    result: List[BgcMethod] = []
    if type in (BgcMethodRestType.ALL, BgcMethodRestType.CALIBRATION):
        method = BgcMethod(
            type=BgcMethodTypeNames.CALIBRATION,
            clarity_name="cal_method_2",
            temperatures=[
                IsocraticTemperaturePair(name=IsocraticTemperatureName.COLUMN_XFER, value=123.4),
            ],
            name="CalMethod",
            flows=[
                IsocraticFlowPair(name=IsocraticFlowName.AIR_FPD, value=120 / 1000),
                IsocraticFlowPair(name=IsocraticFlowName.HC_N2, value=50 / 1000),
            ],
        )
        result.append(method)
    if type in (BgcMethodRestType.ALL, BgcMethodRestType.SCAN):
        method = BgcMethod(
            type=BgcMethodTypeNames.SCAN,
            clarity_name="cal_method_air",
            temperatures=[
                IsocraticTemperaturePair(name=IsocraticTemperatureName.SAMPLE_LINE, value=87.9),
            ],
            name="CalMethod",
            flows=[
                IsocraticFlowPair(name=IsocraticFlowName.AIR_FPD, value=120 / 1000),
                IsocraticFlowPair(name=IsocraticFlowName.WASTE, value=80 / 1000),
            ],
        )
        result.append(method)
    return result


@router.put(
    path="/set-method",
    name="set",
    description="Set all values for a BGC method, overwrites existing method",
)
async def set_bgc_method(value: BgcMethod) -> None:
    pass
