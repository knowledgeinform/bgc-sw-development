from typing import List, TypeAlias

from fastapi import APIRouter

from server.app.core.device_info import FlowName, IsocraticFlowName
from server.app.rest.utils.types import (
    IsocraticFlowPair,
    NameValuePair,
    UnknownPair,
    unknown_pair,
)

router = APIRouter()

FlowStatus: TypeAlias = UnknownPair[FlowName]


@router.get(
    path="/ids",
    description="Get the device ids for all of the gas flows",
)
async def get_ids() -> List[NameValuePair[FlowName, str]]:
    return [NameValuePair(name=name, value="A") for name in FlowName]


@router.get(
    path="/status",
    description="Get the status of all of the gas flows.",
)
async def get_status() -> List[FlowStatus]:
    return [unknown_pair(name) for name in FlowName]


# TBD - part of system settings?
@router.get(
    path="/isocratic_defaults",
    description="Return all isocratic temperature defaults.",
)
async def get_isocratic_defaults() -> List[IsocraticFlowPair]:
    return [IsocraticFlowPair(name=name, value=2.1) for name in IsocraticFlowName]


@router.put(
    path="/set-flows",
    name="set",
    description="Set one or more gas flows",
)
async def set_flows(value: List[IsocraticFlowPair]) -> None:
    pass
