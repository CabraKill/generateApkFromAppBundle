# generateApkFromAppBundle
A *CLI* with a Python script for building **appbundle** and generating **apk**s from it.
Or, as I prefer, a PLI, *Python Line InterFace*.

![PLI](PLI.png)

## How to use it 🎯:
* Install java
* Download the [latest version of bundleTool.jar](https://github.com/google/bundletool/releases) as bundletool.jar
* Run install.bat
* Add the location of bin folder to PATH
* Run:

Command line
```
    generate_apk
```
Bash
```bash
    generate_apk.bat
```
## Why 💡:
In cases where both appbundle and apk are desired, this PLI may be usefull.

Or even when, for some reason like mine, the apk **APK** can't be directly generated from **flutter build apk**.

## Improvements or Suggestions 🚀:
* Add an optional parameter to run on the current location
* Make a script to download the bundletool
* Make cross platform (installation and running)

## ASCII ART generator:
https://patorjk.com/software/taag
