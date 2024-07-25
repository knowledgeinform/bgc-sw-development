from typing import List, TypeAlias
from fastapi import APIRouter
from server.app.core.device_info import DigitalIoName

from server.app.rest.utils.types import NameValuePair, OnOff


router = APIRouter()

# Type checked name value pairs for flow/temperature pairs
DigitalIo: TypeAlias = NameValuePair[DigitalIoName, OnOff]


@router.get(
    path="/status",
    name="status",
    description="Read the status of the digital IO lines",
    response_description="System digital IO values",
)
async def get_status() -> List[DigitalIo]:
    return [DigitalIo(name=name, value=OnOff.OFF) for name in DigitalIoName]
