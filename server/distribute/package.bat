rem Package the application into a One-Folder bundle

cd
pushd frontend
@rem Batch file bails if nothing runs after the ng command
cmd /c ng build --base-href / --allowed-common-js-dependencies sweetalert2
popd
pyinstaller --clean --noconfirm  pyinstaller-bgc-sw.spec

echo Packaged application is in `dist/bgc-sw`
