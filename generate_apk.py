# Python script for build app bundle and generate apks from it.

import os
import pathlib
import tkinter as tk
from tkinter import filedialog
import zipfile
import subprocess
from colored import fg, attr
from pathlib import Path
import webbrowser
# import argparse

CLI_HEADER = '''
 /$$$$$$$      /$$           /$$$$$$
| $$__  $$    | $$          |_  $$_/
| $$  \ $$    | $$            | $$  
| $$$$$$$/    | $$            | $$  
| $$____/     | $$            | $$  
| $$          | $$            | $$  
| $$          | $$$$$$$$     /$$$$$$
|__/          |________/    |______/
'''


def main():
    print(f'%s${CLI_HEADER}%s' % (fg(6),attr(0)))
    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "--debug", "-v", help="If it will generate a debug apk", default=false)
    print("Choose the base flutter project directory\n\n")
    root = tk.Tk()
    root.withdraw()

    choosen_path = filedialog.askdirectory()
    FILE_PATH = Path(choosen_path)
    if(not FILE_PATH):
        print("Directory not choosed")
        return
    SUB_FOLDER = Path("build/app/outputs/bundle/release")
    DESTINATION = FILE_PATH / SUB_FOLDER

    print(f"destination: {DESTINATION}")
    # os.system("copy bundletool.jar \"" + FILE_PATH +
    #           SUB_FOLDER + "bundletool.jar\" /Y")

    subprocess.run('flutter clean',shell=True,cwd=FILE_PATH)
    subprocess.run('flutter build appbundle',shell=True,cwd=FILE_PATH)

    
    if (DESTINATION / "app-release.aab").exists():
        bundleName = "app-release.aab"
    elif (DESTINATION / "app.aab").exists():
        bundleName = "app.aab"
    else:
        print("Bundle file does not exist")
        return
    
    bundleLocation = Path(os.path.dirname(__file__)) / "bundletool.jar" 
    os.system(
        f"java -jar {bundleLocation} build-apks --bundle=\"{DESTINATION / bundleName}\" --output=\"{DESTINATION / 'app.apks'}\" --mode=universal")

    def apk_path(file):
        apks = DESTINATION / file
        print(f"APKS location: {apks}")
        return apks
    with zipfile.ZipFile(apk_path("app.apks"), 'r') as zip_ref:
        zip_ref.extractall(apk_path(""))

    os.chdir(FILE_PATH / SUB_FOLDER)
    os.listdir()
    webbrowser.open(os.getcwd())
    input("\n\n...........Press to exit...........")


if __name__ == "__main__":
    main()
