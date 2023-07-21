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

    def move(self):
        pyautogui.moveTo(x=self.param[0], y=self.param[1], duration=0.5)

    def click(self, button='primary'):
        self.move()
        pyautogui.click(button=button)

    def right_click(self):
        self.click(button='right')

    def type(self):
        pyautogui.write(self.param)

    def wait(self):
        pyautogui.sleep(self.param)

    def press(self):
        pyautogui.press(self.param)

    def scroll(self):
        pyautogui.scroll(self.param)
