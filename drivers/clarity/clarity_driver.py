from __future__ import annotations

from typing import Final


# Should be a ClassVar but we can't use it for an initial value then
DEFAULT_EXE_PATH: Final[str] = r"C:\Clarity\Bin\Clarity.exe"


class ClarityDriver:
    def __init__(self, exe_path: str = DEFAULT_EXE_PATH) -> None:
        self._exe_path = exe_path

    @property
    def exe_path(self) -> str:
        return self._exe_path

    @exe_path.setter
    def exe_path(self, value: str) -> None:
        self._exe_path = value
