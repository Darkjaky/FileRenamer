import os
from .Formatter import format_filename


def rename_files(path, files):
    os.chdir(path)
    for file in files:
        os.rename(file, format_filename(file))
