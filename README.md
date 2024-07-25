# BGC SW Setup

## Overview

## Environment Setup

### General

This project uses:

* [Python](https://www.python.org) version 3.11 or greater (`pyproject.toml` deploy dependency)
* [Poetry](https://python-poetry.org/docs/) 1.4.1 to manage dependencies and virtual environment (command line install below)
  * See [RealPython](https://realpython.com/dependency-management-python-poetry/) for a good discussion of dependency management with Poetry.
  * NOTE: Poetry versions after 1.4.1 change the format of the `poetry.lock` file which may affect tooling.  This note will be removed when this incompatibility is no longer a problem.
* [mypy](https://mypy.readthedocs.io/en/latest/index.html) for type checking (`pyproject.toml`) dependency
* [Ruff](https://pypi.org/project/ruff/) for linting and formatting (`pyproject.toml` dev dependency)
* [pre-commit](https://pypi.org/project/pre-commit/) hooks to maintain formatting adherence (command line install below)

It's recommended you install support for the formatting and linting tools in your IDE so the pre-commit hooks rarely need to actually do anything.

### Windows vs Linux

The commands in this README are generally written for Linux/Mac users.  A general familiarity with both operating systems is assumed.   That said, where commands differ significantly they will be provided for both operating systems.

Here are a few common differences.

| Area                         | Linux                  | Windows                    |
| ---------------------------- | ---------------------- | -------------------------- |
| Paths                        | `./a/b/...`            | `.\a\b\...`                |
| Python                       | `python3`              | `python`                   |
| Activate Virtual Environment | `./.venv/bin/activate` | `.\.venv\Scripts\activate` |
| Environment Variables        | `VAR=value`            | `set VAR=value`            |

### Python Install

Python is available [here](https://www.python.org/downloads/).  See `pyproject.toml` for specifics.

Optionally, if you are also developing other projects that depend on other versions of Python, you can install *pyenv*, a Python version manager which allows you install, manage, and switch among different versions of Python.

See: [pyenv](https://realpython.com/intro-to-pyenv/) for instructions.

**NOTE:** If there are SSL Verification errors with any of the commands that follow, perform the following commands (you may also want to permanently add/replace PIP_CERT in your environment).  In addition, there may be problems unless you are not on the wireless VPN.

```terminal
 PIP_CERT=<path-to-project>/cafile-with-apl.pem
 poetry config certificates.artifactory-pypi.cert <path-to-project>/cafile-with-apl.pem
 poetry config certificates.artifactory-apl.cert <path-to-project>/cafile-with-apl.pem
```

These `poetry` commands update your global configuration.   `poetry config --local` still seems to put them in the global configuration and not in `poetry.toml
`
**NOTE:** If there are timeouts setting up the virtual environment, perform the following command (you may also wan to permanently
add/replace PIP_DEFAULT_TIMEOUT in your environment).

```terminal
PIP_DEFAULT_TIMEOUT=999
```

### Command Line

#### Poetry

**Important** Install the `poetry` using the version specified above [General](#general) above.

e.g. With pip use `pip install poetry==<version>` or official installer use `curl ... | python3 - --version <version>`

#### pre-commit

Install `pre-commit` and configure pre-commit hooks in your local repo:

* The `pip install pre-commit` installs the tool into your current python environment (your virtual environment inherits this).   As such, it below will have to be repeated for all installations of python you plan to use for virtual environments.  If however, you are on a Mac, you can replace `pip install pre-commit` below with `brew install pre-commit` to make `pre-commit` available globally, and hence in all python installations.

```bash
pip install pre-commit
pre-commit install --install-hooks
```

#### poetry

Poetry is available [here](https://python-poetry.org/docs/), to manage dependencies and virtual environments.  The easiest way is to install Poetry for all Python versions.  Use the Poetry site's *With the official installer* section, *Install Poetry (advanced)* subsection to install the specific version.  Methods other than the official installer typically install for the active version of Python, which is ok too.

In your project root, create a virtual environment in `.venv` (done via `poetry.toml` settings) and install all dependencies from the project's `poetry.lock`:

```bash
poetry install

# NOTE: dev dependencies can be omitted by using 'poetry install --no-dev'

# Confirm dependencies and subdependencies were installed into your virtual environment

poetry show

# Verify python version and confirm dependencies from within the virtual environment

./.venv/bin/activate
python3 -V
poetry show

# NOTE: you can also spawn a shell in the virtual environment using 'poetry shell' and exit it with 'exit' but the
# activate script changes the prompt to notify you that you are in the virtual environment
```

The resulting virtual environment can be used for your pygraphsf development efforts (i.e., configure your IDE to
use the above virtual environment).

**NOTE:** If Poetry is not using the active version of Python use `poetry env use <path-to-python-executable>` to specify
exactly which python executable to use to create the virtual environment.

#### Other tools / commands

NOTE: In the commands below, if you have already activated your virtual environment you can omit the `poetry run` portion of each command below (e.g. `pytest` would suffice to run the unit tests).

Run unit tests (configured in `pyproject.toml`):

```console
poetry run pytest
```

Run test coverage for the unit tests (this will also run the unit tests) and generate html coverage report (outputs
html results to ./htmlcov subdirectory):

```console
poetry run coverage run --pylib --source=TBD-m pytest --junitxml build/test_results/bgcsw_test_results.xml
poetry run coverage xml -o build/coverage/bgc_coverage.xml
poetry run coverage html
```

Run the python type-checking linter (configured in `pyproject.toml`):

```console
poetry run mypy
```

Run the python linter (configured in `pyproject.toml`):

* If you use Ruff's `--fix` option to automatically fix some violations be sure to inspect all changes and verify unit tests pass afterwards.

``` console
poetry run ruff .
```

Run the code formatter (configured in `pyproject.toml`):

``` console
poetry run ruff format .
```

### VSCode

Download VSCode [here](https://code.visualstudio.com/).

Open the project

```bash
cd /path/to/<project>
code .
```

Support for the following is configured for VS Code:

* Recommended plugins based on repo contents and standards
  * Install these using Extensions : Filter on @recommended : Workspace Recommendations
* Support for performing common development tasks (`cmd + shift + p` `Tasks: Run Task`)

If the local virtualenv (the one you created in the previous section) isn't automatically detected, set the active Python Interpreter to your virtualenv. In the IDE, run `cmd + shift + p` and type `Python: Select Interpreter`. A list will be displayed - select one that looks like .venv/bin/python.

A notification may show that asks to install the linter - MyPy - in your virtual env. Click install. If this does not show,
you make need to try saving a source file to activate the IDE linting, after which it will ask to install.

### VS Code Recommendations

* Install the recommended extensions (see `.vscode/extensions.json`)
* Enable the following settings in user settings:
  * Pylance > Python > Analysis > Inlay Hints: Function Return Types
  * Pylance > Python > Analysis > Inlay Hints: Variable Types
* Command: `Ruff fix all auto-fixable problems` is your friend as is `Ruff format imports`

## Front End Setup

### Installation

Installation instructions are at [Angular Setup](https://angular.io/guide/setup-local).  Versions specified are based on compatibility defined [here](https://angular.io/guide/versions).

Powershell as administrator, or using VS code's terminal as admin, will be used for all code commands below.

1. All operations should be done in the frontend directory.

```console
  cd frontend\
```

2. Install Node.js version `^18.16` (`>=18.16.0 && <19.0.0`)

* [NodeJS](https://nodejs.org/en/)
* This will install 'node' and 'npm'. To test that both have installed correctly:
  * `node -v`
  * `npm -v`

3. Set up APL certificate to ensure we can run npm commands on the network/VPN

* Follow steps in
  * [Development Tool Guide - Node.js](https://aplprod.servicenowservices.com/now/nav/ui/classic/params/target/kb_view.do%3Fsysparm_article%3DKB0015038)
  * [How to Use APL Root CA Cert with Node.js](https://aplweb.jhuapl.edu/services/IT%20Services%20Documents/Howto_Use_Root_CA_Cert_with_Node.js.pdf) (see summary below)

  * Download cert file

```console
npm config set cafile [Path_To_Cert]\JHUAPL-MS-Root-CA-05-21-2038-B64-text.cer
```

* Add new 'NODE_EXTRA_CA_CERTS' environmental user variable with cert path above.

4. Update npm

* Ensure that npm is using https

```console
npm set registry=https://registry.npmjs.org/
```

5. Install Angular CLI (version 15.2.9)

```console
npm install -g @angular/cli@15.2.9
```

6. Install/update all the modules from node_modules folder

```console
npm install
# NOTE: may take up to 30 minutes to complete
```

* Use `ng version` to output the versions for Angular CLI and Node to ensure they are the correct versions as stated above.

### Front End Commands

#### Run the dev server (must be in /frontend directory)

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

#### Lint and format before merging

```console
ng lint --fix
```

#### Update frontend's api directory

* Run if /server/[name] api has been updated

```console
npm run generate-[name]-api
```

#### Tailwind CSS

Tailwind is a tool that allows CSS formatting and placing of components in the HTML code.

Learn more [here](https://tailwindcss.com/docs/guides/angular)

## Server Setup

### Run Server

1. For directions below, this will run /server/controller services. In the future, there may be more components added to /server, so adjust accordingly.

``` console
poetry shell
watchfiles "uvicorn server.app.main:app" .
```

Mac/Linux cam also use the following command.

```console
poetry shell
uvicorn server.app.main:app --reload
```

We use various
[Asyncio Subprocess Commands](https://docs.python.org/3.11/library/asyncio-subprocess.html?highlight=create_subprocess_exec#asyncio.create_subprocess_exec) to interface to Clarity.   On Windows this must be done with a `ProactorEventLoop`.  Unfortunately
`uvicorn --reload` causes the event loop to be a `SelectorEventLoop` which doesn't support the subprocess calls.
See <https://stackoverflow.com/questions/70568070/running-an-asyncio-subprocess-in-fastapi-results-in-notimplementederror>.

1. Navigate to `http://localhost:8000/docs` to view Swagger page.

## Development Workflow

You want to add a feature of fix a bug:

1. In Gitlab, create a new issue. Name the issue with a descriptive feature or bug.
2. On the issue page, click ‘Create merge request’ button. This will create a new branch, ideally one that branches off of ‘Development’.
3. In your IDE, run ‘git fetch’ to access your newly created branch.
4. Work on your branch, add your features/fix the bugs.
5. In your IDE, run ‘git fetch’ to see if you need to update your branch with any new additions to the ‘Development’ branch. If so, pull the new changes from the Development branch, go back to your branch, and run ‘git merge development’.
6. Once done, commit/merge your changes on your branch.
7. On the merge request that was created when you created your branch, Fill out the two questions ‘What new capabilities does this branch add? Why does this branch need to be merged?’ and ‘How should reviewers test your branch? Please include specific instructions on how to build and run your branch.’
8. On your merge request, mark the Merge Request as ‘Ready’ (the settings button next the Code button on the upper right).
9. Add your Reviewers to your Merge Request. Typically, this is Jim, Christa, and myself.
10. Once one of us approves the branch, it can then be merged. Ideally by you, but can be other people.
