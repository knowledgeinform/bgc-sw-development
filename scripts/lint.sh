#!/usr/bin/env bash

set -e
set -x

# run the script from the right location no matter where you run it from
SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $SCRIPTDIR/..

# mypy ...
poetry run ruff format --check --diff .
poetry run ruff check . --exclude */in_progress/*
