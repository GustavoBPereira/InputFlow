class FileManager:
    def __init__(self, file_name):
        self.file = open(file_name, 'r')

    def next_line(self):
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
