from fastapi import APIRouter

from server.app.rest.routes import (
    bgc_method,
    clarity,
    digital_io,
    flame_control,
    gas_flow,
    system,
    temperature,
)

# Define system router to create paths to all but last hop(s) to service endpoints
router = APIRouter()
router.include_router(router=bgc_method.router, tags=["bgc-method"], prefix="/bgc-method")
router.include_router(router=clarity.router, tags=["clarity"], prefix="/clarity")
router.include_router(router=digital_io.router, tags=["digital-io"], prefix="/digital-io")
router.include_router(router=flame_control.router, tags=["flame-control"], prefix="/flame-control")
router.include_router(router=gas_flow.router, tags=["gas-flow"], prefix="/gas-flow")
router.include_router(router=system.router, tags=["system"], prefix="/system")
router.include_router(router=temperature.router, tags=["temperature"], prefix="/temperature")
