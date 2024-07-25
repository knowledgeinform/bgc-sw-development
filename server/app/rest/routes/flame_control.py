from fastapi import APIRouter
from server.app.rest.utils.types import OnOff


router = APIRouter()


@router.get(
    path="/temperature",
    name="temperature",
    description="Read the flame controller temperature",
    response_description="TBD This might not be just a value but for now...",
)
async def get_temperature() -> float:
    return 123.4


@router.put(
    path="/control/{state}",
    name="set",
    description="Turn the flame on or off",
)
async def set_state(state: OnOff) -> None:
    # validate the parameters and store the bgc method
    pass
