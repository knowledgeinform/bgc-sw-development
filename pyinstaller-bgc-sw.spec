# -*- mode: python ; coding: utf-8 -*-

PROJECT_NAME = "bgc-sw"

a  =  Analysis(
    ["server/distribute/launch.py"],
    pathex = [],
    binaries = [],
    datas = [("./frontend/dist/bgc-frontend/", "./frontend/dist/bgc-frontend/")],
    hiddenimports = [],
    hookspath = [],
    hooksconfig = {},
    runtime_hooks = [],
    excludes = [],
    noarchive = False,
)

pyz  =  PYZ(a.pure)

exe  =  EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries = True,
    name = PROJECT_NAME,
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
    a.datas,
    strip = False,
    upx = True,
    upx_exclude = [],
    name = PROJECT_NAME,
)
