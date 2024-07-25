import os
import pathlib
import sys
from fastapi.staticfiles import StaticFiles
import uvicorn
from server.app.main import app

"""
Program to launch the application using uvicorn.
Performs extra app configuration to serve up the static frontend code.
Adapted from Concerto server/app/main.py.
Works if launched from a development environment or from a pyinstaller bundled executable.
"""


def is_pyinstaller_bundled() -> bool:
    """
    Determine if we're running as a pyinstaller bundled application.

    See https://pyinstaller.org/en/stable/runtime-information.html
    """
    return getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS")


# override default swagger and redoc URLs. Provide paths to local, static mounted static files
# @app.get("/docs", include_in_schema=False)
# async def custom_swagger_ui_html() -> HTMLResponse:
#     return get_swagger_ui_html(
#         openapi_url=app.openapi_url,  # type: ignore
#         title=app.title + " - Swagger UI (offline)",
#         oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
#         swagger_js_url=f"{API_DOC_STATIC_FILE_MOUNT_PATH}/swagger-ui-bundle.js",
#         swagger_css_url=f"{API_DOC_STATIC_FILE_MOUNT_PATH}/swagger-ui.css",
#         swagger_favicon_url=f"{API_DOC_STATIC_FILE_MOUNT_PATH}/favicon.ico",
#     )

# @app.get("/redoc", include_in_schema=False)
# async def redoc_html() -> HTMLResponse:
#     return get_redoc_html(
#         openapi_url=app.openapi_url,  # type: ignore
#         title=app.title + " - ReDoc (offline)",
#         redoc_js_url=f"{API_DOC_STATIC_FILE_MOUNT_PATH}/redoc.standalone.js",
#         redoc_favicon_url=f"{API_DOC_STATIC_FILE_MOUNT_PATH}/favicon.ico",
#         with_google_fonts=False,
#     )


# locate the static frontend no matter if we're bundled or running natively
#
if is_pyinstaller_bundled():
    project_base = pathlib.Path(sys._MEIPASS)  # type: ignore
else:
    project_base = pathlib.Path(pathlib.Path(__file__))
    while project_base.name != "bgc-sw":
        project_base = project_base.parent
frontend_dir = pathlib.Path(project_base, "frontend", "dist", "bgc-frontend")

assert pathlib.Path(frontend_dir, "index.html").is_file(), f"{frontend_dir}{os.path.sep}index.html doesn't exist"

# maestro = pathlib.Path(pathlib.Path(__file__).parent.parent.parent, "maestro", "dist")
# static_doc_resources_path = pathlib.Path(pathlib.Path(__file__).parent.parent, "static")
# server/static had favicon.ico  redoc.standalone.js  swagger-ui.css  swagger-ui-bundle.js
# try:
#     # /static must be mounted first, so that the maestro static mount at '/' doesn't doesn't overridden
#     app.mount(
#         API_DOC_STATIC_FILE_MOUNT_PATH,
#         StaticFiles(directory=static_doc_resources_path),
#         name="static",
#     )
# except Exception as e:
#     print(e)
#     pass


# in case we want to build documentation using Sphinx and just have it...
# try:
#     # This will only work with built paths (not in dev mode)
#     documentation_path = pathlib.Path(
#         pathlib.Path(__file__).parent.parent.parent, "maestro", "dist", "manual"
#     )

#     app.mount(
#         "/manual",
#         StaticFiles(directory=str(documentation_path), html=True),
#         name="manual",
#     )
# except Exception as e:
#     logger.debug(f"Exception mounting manual {e}")
#

# Mount the frontend static API build for FastAPI to serve
try:
    app.mount(
        path="/",  # rest path from the host:port
        app=StaticFiles(directory=str(frontend_dir), html=True),  # where the files are in the file system
    )
except RuntimeError as e:
    print(e)  # TODO log


def serve_application() -> None:
    host = "localhost"
    port = 4200
    print(f"Running on {host}:{port}...")
    print(f"Docs available at {host}:{port}/docs...")
    uvicorn.run(app, host="0.0.0.0", port=4200)


if __name__ == "__main__":
    serve_application()
