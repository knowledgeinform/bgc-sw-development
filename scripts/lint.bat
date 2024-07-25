
rem run the script from the right location no matter where you run it from

SET my_path=%~dp0
SET script_path=%my_path:~0, -1%

pushd %script_path%\..

rem mypy ...
poetry run ruff format --check --diff .
poetry run ruff check . --exclude */in_progress/*

popd
