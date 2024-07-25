from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Annotated, Any, Final
from typing import Dict, List
import asyncio

# Should be a ClassVar but we can't use it for an initial value then
DEFAULT_EXE_PATH: Final[str] = r"C:\Clarity\Bin\Clarity.exe"
clarity_demo_path = "C:\\Clarity_Demo\\Bin\\Clarity_Demo.exe"

router = APIRouter()


class ExportRequest(BaseModel):
    filepath: str  # TODO this needs to be a name, we'll make {path}/{name}.txt or whatever
    format: str  # ???


async def run_subprocess(command: List[str]) -> Dict[str, Any]:
    # TODO figure out how to get create_subprocess_exec working - this is a better option
    # worked on Jim's Windows Python 3.11.4
    # didn't work on Tzipi's Windows Python 3.11.7 (not sure if python was the issue)
    # didn't work on Ashley's Windows Python 3.11.TBD (not sure if python was the issue)
    # result = await asyncio.create_subprocess_exec(
    #     "echo",
    #     *command,
    #     stdout=asyncio.subprocess.PIPE,
    #     stderr=asyncio.subprocess.PIPE,
    # )
    result = await asyncio.create_subprocess_shell(
        cmd=f"echo {' '.join(command)}",  # just echo would be command/args for now
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await result.communicate()
    if stdout:
        print(f"[stdout]\n{stdout.decode()}")
    if stderr:
        print(f"[stderr]\n{stderr.decode()}")
    return {"returncode": result.returncode, "stdout": stdout.decode(), "stderr": stderr.decode()}


def validate_method(method: str) -> None:
    pass  # TODO eventually this would be in the driver, we need one for existence and one for form


# def validate_file_path(file_path: str, extension: str) -> None:
#     if not file_path.endswith(extension) or not os.path.exists(file_path):
#         raise HTTPException(status_code=400, detail=f"Invalid or non-existent {extension} file path")


@router.post("/start_clarity")
async def start_clarity() -> Dict[str, Any]:
    return await run_subprocess([clarity_demo_path, "hide_splash"])


@router.post("/exit_clarity")
async def exit_clarity() -> Dict[str, Any]:
    return await run_subprocess([clarity_demo_path, "exit"])


@router.post("/cal_apply")
async def cal_apply(
    method: Annotated[str, Query(description="The name of the method to apply")],
) -> Dict[str, str]:
    # validate_file_path(method, ".CAL")
    validate_method(method)
    apply_command = ["cal_apply", method]
    result = await run_subprocess(apply_command)
    if result["returncode"] != 0:
        return {"error": result["stderr"]}
    return {"message": "Calibration applied successfully", "output": result["stdout"]}


@router.post("/cal_save")
async def cal_save() -> Dict[str, str]:
    save_command = [f"{clarity_demo_path} cal_save"]
    result = await run_subprocess(save_command)
    if result["returncode"] != 0:
        return {"error": result["stderr"]}
    return {"message": "Calibration saved successfully", "output": result["stdout"]}


@router.post("/cal_save_as")
async def cal_save_as(
    method: Annotated[str, Query(title="The name to save the current method under")],
) -> Dict[str, str]:
    validate_method(method)
    # validate_file_path(filepath, ".CAL")
    save_as_command = [clarity_demo_path, "cal_save_as", method]
    result = await run_subprocess(save_as_command)
    if result["returncode"] != 0:
        return {"error": result["stderr"]}
    return {"message": "Calibration saved successfully", "output": result["stdout"]}


@router.post("/cal_type")
async def cal_type(calibration_type: str) -> Dict[str, str]:
    valid_chars = set("_,UIENSD")
    if not all(c in valid_chars for c in calibration_type):
        raise HTTPException(status_code=400, detail="Invalid calibration type characters")
    cal_type_command = [clarity_demo_path, "cal_type", calibration_type]
    result = await run_subprocess(cal_type_command)
    if result["returncode"] != 0:
        return {"error": result["stderr"]}
    return {"message": "Calibration type changed successfully", "output": result["stdout"]}


@router.post("/clear_cal")
async def clear_cal() -> Dict[str, str]:
    clear_cal_command = [clarity_demo_path, "clear_cal"]
    result = await run_subprocess(clear_cal_command)
    if result["returncode"] != 0:
        return {"error": result["stderr"]}
    return {"message": "Calibration cleared successfully", "output": result["stdout"]}


@router.post("/cfg")
async def cfg(filepath: str) -> Dict[str, str]:
    # validate_file_path(filepath, ".CFG")
    cfg_command = [clarity_demo_path, "clarity_cfg_command", filepath]
    result = await run_subprocess(cfg_command)
    if result["returncode"] != 0:
        return {"error": result["stderr"]}
    return {"message": "CFG file loaded successfully", "output": result["stdout"]}


@router.post("/abort")
async def abort_analysis(value: int) -> Dict[str, str]:
    if value not in [1, 2, 4, 8]:
        raise HTTPException(status_code=400, detail=f"Invalid instrument value: {value}")
    abort_command = [clarity_demo_path, "abort", str(value)]
    result = await run_subprocess(abort_command)
    if result["returncode"] != 0:
        return {"error": result["stderr"]}
    return {"message": f"Abort command sent to Instruments with value: {value}"}


@router.post("/export_results/")
async def export_results(request: ExportRequest) -> Dict[str, str]:
    export_command = [clarity_demo_path, "export_results", request.filepath, request.format]
    result = await run_subprocess(export_command)
    if result["returncode"] != 0:
        return {"error": result["stderr"]}
    return {"message": "Results exported successfully", "output": result["stdout"]}


@router.post("/export_results_dbf/")
async def export_results_dbf(request: ExportRequest) -> Dict[str, str]:
    export_dbf_command = [clarity_demo_path, "export_results_dbf", request.filepath]
    result = await run_subprocess(export_dbf_command)
    if result["returncode"] != 0:
        return {"error": result["stderr"]}
    return {"message": "Results exported in DBF format successfully", "output": result["stdout"]}


@router.post("/export_run_time/")
async def export_run_time(request: ExportRequest) -> Dict[str, str]:
    export_rt_command = [clarity_demo_path, "export_run_time", request.filepath, request.format]
    result = await run_subprocess(export_rt_command)
    if result["returncode"] != 0:
        return {"error": result["stderr"]}
    return {"message": "Run time exported successfully", "output": result["stdout"]}
