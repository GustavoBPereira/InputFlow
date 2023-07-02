class ScriptManager:
    def __init__(self, command: [str, str]):
        self.command = command[0]
        self.param = command[1]

    def execute(self):
        method = self.correct_method()
        method()

    def correct_method(self):
        return getattr(self, self.command)

    def click(self):
        ...

    def type(self):
        ...

    def wait(self):
        ...

    def press(self):
        ...
