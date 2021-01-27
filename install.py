import os

PATH = "%PROGRAMFILES%"
FOLDER = "generate_apk"
DIRECTORY = PATH + "\\" + FOLDER
FILENAME = "generate_apk.py"
os.chdir("C:\\Program Files")
if(not os.path.exists(FOLDER)):
    os.system("mkdir " + FOLDER)
    print(f"Directory {DIRECTORY} created.")
# os.system(f"copy {FILENAME} \"{DIRECTORY}\\{FILENAME}\"")
# os.system(f"copy bundle_tool.jar \"{DIRECTORY}\\bundle_tool.jar\"")
