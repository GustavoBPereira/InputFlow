from managers import FileManager, ScriptManager
from pathlib import Path

file_path = Path() / 'script_test.txt'
file = FileManager(file_path.absolute())

while True:
    command_and_param = file.next_line()
    if command_and_param:
        ScriptManager(*command_and_param).execute()
    else:
        break
