import os

def list_directory_path(path):
    for root, dirs, files in os.walk(path):
        print("Directory:", root)
        for file in files:
            print("File:", os.path.join(root, file))
        for dir in dirs:
            print("Subdirectory:", os.path.join(root, dir))


list_directory_path("./")

