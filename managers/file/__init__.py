class FileManager:
    def __init__(self, file_name):
        self.file = open(file_name, 'r')

    def next_line(self):
        line = self.file.readline()
        if not line:
            return False
        return line.strip().split(':>')
