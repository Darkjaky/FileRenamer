import os


def get_files_from_directory(path):
    files = (file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)))
    os.chdir(path)
    return files
