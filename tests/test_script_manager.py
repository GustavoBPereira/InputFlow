from unittest import TestCase
from unittest.mock import patch
from managers.script import ScriptManager


class TestScriptManager(TestCase):

    @patch('pyautogui.moveTo')
    @patch('pyautogui.click')
    def test_execute_click_method(self, mock_click, mock_moveto):
        script_manager = ScriptManager('click', [960, 540])
        script_manager.execute()
        mock_click.assert_called_once()
        mock_moveto.assert_called_once()

    @patch('pyautogui.write')
    def test_execute_type_method(self, mock):
        script_manager = ScriptManager('type', 'hello world')
        script_manager.execute()
        mock.assert_called_once()

    @patch('time.sleep', return_value=None)
    def test_execute_wait_method(self, mock):
        script_manager = ScriptManager('wait', 2)
        script_manager.execute()
        mock.assert_called_once()

    @patch('pyautogui.press')
    def test_execute_press_method(self, mock):
        script_manager = ScriptManager('press', 'enter')
        script_manager.execute()
        mock.assert_called_once()

    def test_get_click_method(self):
        script_manager = ScriptManager('click', [960, 540])
        self.assertEqual(script_manager.correct_method().__name__, 'click')

    def test_get_type_method(self):
        script_manager = ScriptManager('type', 'hello world')
        self.assertEqual(script_manager.correct_method().__name__, 'type')

    def test_get_wait_method(self):
        script_manager = ScriptManager('wait', 2)
        self.assertEqual(script_manager.correct_method().__name__, 'wait')

    def test_get_press_method(self):
        script_manager = ScriptManager('press', 'enter')
        self.assertEqual(script_manager.correct_method().__name__, 'press')
