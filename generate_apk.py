# Python script para copiar o bundletool para a pasta de build do appbundle e criar os apks
# Programmer: Raphael

import os
import tkinter as tk
from tkinter import filedialog
import zipfile


def main():
    os.system("color b")
    print("Choose the base flutter project directory\n\n")
    root = tk.Tk()
    root.withdraw()

    FILE_PATH = filedialog.askdirectory()
    if(not FILE_PATH):
        print("Directory not choosed")
        return
    SUB_FOLDER = "/build/app/outputs/bundle/release"
    DESTINATION = FILE_PATH + SUB_FOLDER
    INSTALATION="\"C:\\Program Files\\generateApkFromAppBundle\""

    print("destination: " + DESTINATION)
    # os.system("copy bundletool.jar \"" + FILE_PATH +
    #           SUB_FOLDER + "bundletool.jar\" /Y")
    os.chdir(FILE_PATH)
    os.system("flutter build appbundle")
    os.system(
        f"java -jar {INSTALATION}\\bundletool.jar build-apks --bundle=\"{FILE_PATH}{SUB_FOLDER}/app-release.aab\" --output=\"{FILE_PATH}{SUB_FOLDER}/app.apks\" --mode=universal")

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
