import asyncio
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator, Final, Tuple

from fastapi import FastAPI
import uvicorn

from server.app.async_template_stuff import SubsystemController, XyzDeviceDriver
from server.app.rest.routes.api import router as api_router

API_PREFIX: Final[str] = "/api"


# One global controller.   Could just use XyzHwController() everywhere too but that does a Dict lookup every time
subsystem_controller: SubsystemController


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:
    """
    Method that FastAPI will call for startup/shutdown.
    See https://fastapi.tiangolo.com/advanced/events/
    """

    print("FastAPI startup...")
    global subsystem_controller
    subsystem_controller = SubsystemController()
    asyncio.create_task(subsystem_controller.enable_monitoring(True))
    print("FastAPI startup complete...")
    yield
    print("FastAPI shutdown...")
    await subsystem_controller.enable_monitoring(False)
    print("FastAPI shutdown complete...")


app = FastAPI(lifespan=lifespan)


@app.get("/api/xyz/status")
async def xyz_status() -> Tuple[XyzDeviceDriver.Status, ...]:
    """Fictional API that would return the status of some set of XyzDeviceDrivers.   just as example"""
    return await subsystem_controller.status()


def get_application() -> FastAPI:
    application = FastAPI(
        title="bgc-hw",
        debug=False,
        version="0.0.1",
        lifespan=lifespan,
    )
    # application.add_exception_handler(http_error_handler)
    application.include_router(api_router, prefix=API_PREFIX)
    return application


app = get_application()

if __name__ == "__main__":
    host = "localhost"
    port = 8000
    print(f"Docs available at {host}:{port}/docs...")
    uvicorn.run(app, host="localhost", port=port)
