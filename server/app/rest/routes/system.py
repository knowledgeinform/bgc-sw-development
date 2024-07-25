from fastapi import APIRouter

from server.app.rest.utils.types import UNKNOWN_VALUE, UnknownValue


router = APIRouter()


@router.get(
    path="/status",
    description="Return aggregated system status.",
    response_description="TBD maybe this aggregates all of the status from the other endpoints to save on traffic",
)
async def get_status() -> UnknownValue:
    return UNKNOWN_VALUE
