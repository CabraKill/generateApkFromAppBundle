# Python script for build app bundle and generate apks from it.

import os
import tkinter as tk
from tkinter import filedialog
import zipfile
import subprocess
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
    os.system("color b")
    print(CLI_HEADER)
    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "--debug", "-v", help="If it will generate a debug apk", default=false)
    print("Choose the base flutter project directory\n\n")
    root = tk.Tk()
    root.withdraw()

    FILE_PATH = filedialog.askdirectory()
    if(not FILE_PATH):
        print("Directory not choosed")
        return
    SUB_FOLDER = "/build/app/outputs/bundle/release"
    DESTINATION = FILE_PATH + SUB_FOLDER

    print("destination: " + DESTINATION)
    # os.system("copy bundletool.jar \"" + FILE_PATH +
    #           SUB_FOLDER + "bundletool.jar\" /Y")
    subprocess.run(['flutter','clean'],shell=True,cwd=FILE_PATH)
    subprocess.run(['flutter','build','appbundle'],shell=True,cwd=FILE_PATH)
    
    if os.path.exists(f"{FILE_PATH}{SUB_FOLDER}/app-release.aab"):
        bundleName = "app-release.aab"
    elif os.path.exists(f"{FILE_PATH}{SUB_FOLDER}/app.aab"):
        bundleName = "app.aab"
    else:
        print("Bundle file does not exist")
        return
    os.system(
        f"java -jar {os.path.dirname(__file__)}\\bundletool.jar build-apks --bundle=\"{FILE_PATH}{SUB_FOLDER}/{bundleName}\" --output=\"{FILE_PATH}{SUB_FOLDER}/app.apks\" --mode=universal")

    def apk_path(file):
        apks = DESTINATION + "/" + file
        print("APKS location: "+apks)
        return apks
    with zipfile.ZipFile(apk_path("app.apks"), 'r') as zip_ref:
        zip_ref.extractall(apk_path(""))

    os.chdir(FILE_PATH+SUB_FOLDER)
    os.system("dir")
    os.system(f"start .")
    input("\n\n...........Press to exit...........")


if __name__ == "__main__":
    main()
