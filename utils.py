import os
from datetime import datetime

from managers import FileManager, ScriptManager
from managers.file import FileEnd
from managers.inspector import start_mouse_inspector


def run_by_file_path(path):
    file_manager = FileManager(path)
    while True:
        try:
            command_and_param = file_manager.next_line()
            if command_and_param:
                print(f'{command_and_param[0]} : ', end='')
                print(command_and_param[1], sep=',')
                ScriptManager(*command_and_param).execute()
        except FileEnd:
            break


def run_mouse_inspector():
    positions = start_mouse_inspector()
    with open('mouse_history.txt', 'w') as f:
        for position in positions:
            f.writelines(f'click >>> {position["x"]},{position["y"]}\n')


def display_cli_interface(files):
    os.system('cls' if os.name == 'nt' else 'clear')

    print("""
    ____                  __  ________             
   /  _/___  ____  __  __/ /_/ ____/ /___ _      __
   / // __ \/ __ \/ / / / __/ /_  / / __ \ | /| / /
 _/ // / / / /_/ / /_/ / /_/ __/ / / /_/ / |/ |/ / 
/___/_/ /_/ .___/\__,_/\__/_/   /_/\____/|__/|__/  
         /_/
""")
    print("  Escolha o número entre colchetes do arquivo para executar \n")

    for i, file in enumerate(files):
        print(f'[{i + 1}] {file.name}')

    print(
        '\n'
        '=========================================================\n'
        '[0] Para iniciar a captura do mouse\n\n'
        'Quando ativo, sempre que teclar "0" a posição atual do mouse\n'
        'será registrada, para terminar, tecle "esc".\n'
        '\n'
        'Ao teclar "esc" será gerado um arquivo mouse_history.txt\n'
        'com todas as cordenadas do mouse, quando teclou "0"\n'
        '\n'
    )
