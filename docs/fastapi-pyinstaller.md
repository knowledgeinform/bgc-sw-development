# Setting up a FastAPI project to use pyinstaller

These notes were generously provided by Miles Stewart.

Pyinstaller works best with Python 3.9 and above when using FastAPI.

## Install

Install `pyinstaller` to your environment.

``` terminal
pip install pyinstaller
````

* [ ] **TBD** should we just make this a developmental dependency? or let those doing it by hand or the CI system just pip install it?

## .spec file setup

Create a `\<app name>.spec`` file in the root of your python project. Critical pieces to consider are the first, second parameters, and the`hiddenimports` under the Analysis object.

1. path to the entry Python file (wherever FastAPI is spun up, sometimes source). example here is `app/main.py``
2. path that contains the source code. example here is `app``

Hidden imports will be where you specify any packages that are not automatically picked up by Analysis.

Unfortunately, this is usually only found out after creating the executable and attempting to run it

Under EXE you'll want to specify the name of the executable.

``` python
# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(5000)

block_cipher  =  None


a  =  Analysis(
    ['app\\main.py'],
    pathex = ['./app'],
    binaries = [],
    hiddenimports = ['main'],
    excludes = [],
    win_no_prefer_redirects = False,
    win_private_assemblies = False,
    cipher = block_cipher,
    noarchive = False,
)
pyz  =  PYZ(a.pure, a.zipped_data, cipher = block_cipher)

exe  =  EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries = True,
    name = '<app name>',
    debug = False,
    bootloader_ignore_signals = False,
    strip = False,
    upx = True,
    console = True,
    disable_windowed_traceback = False,
    argv_emulation = False,
    target_arch = None,
    codesign_identity = None,
    entitlements_file = None,
)
coll  =  COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip = False,
    upx = True,
    upx_exclude = [],
    name = '<app name>',
)

```

## Building and running the executable

You will then run

``` terminal
pyinstaller --clean --noconfirm  <app name>.spec
```

This will generate a `dist` folder and subsequent library files and executable.
You should be able to run the .exe or .sh directly that is generated to run the app. For ease of
use for Windows users you may just want to create a .bat file that runs the script and auto-opens the default browser.

This batch script can also be useful for setting environment variables, etc to modify the behavior of the app for desktop use.

An example .bat below:

``` bat
start "" "http://localhost"
vims.exe
```

## Service up JS build with FastAPI

`ng build --base-href <whatever> --prod`

Wherever you are instantiating the FastAPI app -

``` terminal
app = FastAPI()
app.mount("/", StaticFiles(directory="dist", html=True), name="dist")
```

`dist/` being a folder at the same level where you run the python script
`dist` should contain the output of the js build (everything under the SPA folder in this case, but not the spa folder itself)

## Building to a single EXE Eventually

See [Building to One File](<https://pyinstaller.org/en/stable/operating-mode.html?highlight> = single%20file#bundling-to-one-file)
