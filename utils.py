import os

from managers import FileManager, ScriptManager


def run_by_file_path(path):
    file_manager = FileManager(path)
    while True:
        command_and_param = file_manager.next_line()
        if not command_and_param:
            break
        ScriptManager(*command_and_param).execute()


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
        print(f'[{i+1}] {file}')
