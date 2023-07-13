import os

from managers import FileManager
from utils import run_by_file_path, display_cli_interface, run_mouse_inspector

close_app = False

files = [file for file in FileManager.list_files(os.getcwd())]
while not close_app:
    display_cli_interface(files)
    answer = int(input('>>>'))

    if answer == 0:
        run_mouse_inspector()
    else:
        run_quantity = int(input('Quantas vezes quer executar?'))
        runs = 1
        for c in range(0, run_quantity):
            display_cli_interface(files)
            print(f'[{runs}/{run_quantity}]')
            runs += 1
            run_by_file_path(files[answer - 1])
