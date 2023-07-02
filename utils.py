from managers import FileManager, ScriptManager


def run_by_file_path(path):
    file_manager = FileManager(path)
    while True:
        command_and_param = file_manager.next_line()
        if not command_and_param:
            break
        ScriptManager(*command_and_param).execute()
