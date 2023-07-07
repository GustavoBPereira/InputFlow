import os

from managers import FileManager
from utils import run_by_file_path, display_cli_interface

close_app = False

files = [file for file in FileManager.list_files(os.getcwd())]
while not close_app:
    display_cli_interface(files)
    answer = input('>>>')

    run_by_file_path(files[int(answer) - 1])
