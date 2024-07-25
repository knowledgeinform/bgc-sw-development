# Packaging the Software for distribution

We're using `pyinstaller` to package the software, so `pyinstaller` needs to be installed in the environment.

``` terminal
poetry install --with=package
````

* [ ] **TBD** should we just make this a developmental dependency? or let those doing it by hand or the CI system just pip install it?
  * We can consider this after we get a few miles on the evolving application as one folder
  * See [Building to One Foler](https://pyinstaller.org/en/stable/operating-mode.html?highlight=bundle#bundling-to-one-folder)

Currently, `pyinstaller` builds into an executable bundle which includes a `bgc-sw.exe` and a `_internal/` directory.

* [ ] TODO eventually we can try getting it into a single .exe if required

To that end in order to package the application run the following from the top level project directory:

``` terminal
server\distribute\package.bat
```

The packaged application will be in `dist/bgc-sw`.

To distribute zip up the `bgc-sw` directory into a `bgc-sw.zip`.

* [ ] TODO we need to get a version in there that's created by CI and reported.

The resulting Zip file can be unpacked anywhere an the `bgc-sw/bgc-sw.exe` can be run to run it.

See `docs/fastapi-pyinstaller.md` for some more info.
