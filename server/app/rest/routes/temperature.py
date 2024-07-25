from typing import List
from fastapi import APIRouter
from server.app.core.device_info import IsocraticTemperatureName, TemperatureName

from server.app.rest.utils.types import IsocraticTemperaturePair, TemperaturePair


router = APIRouter()


@router.get(
    path="/status",
    description="Return status of all temperatures.",
    response_description="TBD is this just a list of temperatures...",
)
async def get_temperatures() -> List[TemperaturePair]:
    return [TemperaturePair(name=name, value=78.9) for name in TemperatureName]


# TBD - part of system settings?
@router.get(
    path="/isocratic_defaults",
    description="Return all isocratic temperature defaults",
)
async def get_isocratic_defaults() -> List[IsocraticTemperaturePair]:
    return [IsocraticTemperaturePair(name=name, value=18.7) for name in IsocraticTemperatureName]


@router.put(
    path="/set-temperatures",
    name="set",
    description="Set one or more temperatures.",
)
async def set_temperatures(value: List[IsocraticTemperaturePair]) -> None:
    pass
