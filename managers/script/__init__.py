import pyautogui


class ScriptManager:
    def __init__(self, command: str, param):
        self.command = command
        self.param = param

    def execute(self):
        method = self.correct_method()
        method()

    def correct_method(self):
        return getattr(self, self.command)

    def click(self):
        pyautogui.click(x=self.param[0], y=self.param[1])

    def type(self):
        pyautogui.write(self.param)

    def wait(self):
        pyautogui.sleep(self.param)

    def press(self):
        pyautogui.press(self.param)
