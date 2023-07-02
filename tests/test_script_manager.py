from unittest import TestCase

from managers.script import ScriptManager


class TestScriptManager(TestCase):
    def test_get_click_method(self):
        script_manager = ScriptManager(['click', ['960,540']])
        self.assertEqual(script_manager.correct_method().__name__, 'click')

    def test_get_type_method(self):
        script_manager = ScriptManager(['type', ['hello world']])
        self.assertEqual(script_manager.correct_method().__name__, 'type')

    def test_get_wait_method(self):
        script_manager = ScriptManager(['wait', ['2']])
        self.assertEqual(script_manager.correct_method().__name__, 'wait')

    def test_get_press_method(self):
        script_manager = ScriptManager(['press', ['enter']])
        self.assertEqual(script_manager.correct_method().__name__, 'press')
