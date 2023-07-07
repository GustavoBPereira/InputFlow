import os
from pathlib import Path


class FileManager:
    def __init__(self, file_name):
        self.file = open(file_name, 'r')

    def next_line(self):
        line = self.file.readline()
        if line.strip() == ':>InputFlow':
            line = self.file.readline()
        if not line:
            return False
        command_and_param = line.strip().split(':>')
        return self.sanitize_command_and_param(*command_and_param)

    def sanitize_command_and_param(self, command, param):
        match command:
            case 'click':
                param = [int(cord) for cord in param.split(',')]
            case 'wait':
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
            return f.readline().strip() == ':>InputFlow'
