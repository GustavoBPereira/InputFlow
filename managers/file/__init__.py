import os
from pathlib import Path

from managers.file.exceptions import FileEnd


class FileManager:
    def __init__(self, file_name):
        self.file = open(file_name, 'r')

    def next_line(self):
        line = self.file.readline()
        if line.strip() == 'InputFlow' or line == '\n':
            return False
        if not line:
            raise FileEnd
        line_without_comment = line.strip().split(' #')[0]
        command_and_param = line_without_comment.split(' >>> ')
        return self.sanitize_command_and_param(*command_and_param)

    def sanitize_command_and_param(self, command, param):
        match command:
            case 'click':
                param = [int(cord) for cord in param.split(',')]
            case 'wait':
                param = int(param)
            case 'scroll':
                param = int(param)
        return command, param

    @classmethod
    def list_files(cls, path):
        files = []
        for file in os.listdir(path):
            file_path = Path(path) / file
            if file.endswith('.txt') and cls.is_valid_file(file_path):
                files.append(file_path)
        return files

    @classmethod
    def is_valid_file(cls, file):
        with open(file) as f:
            return f.readline().strip() == 'InputFlow'
