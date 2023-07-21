from unittest import TestCase

import pytest

from managers.file import FileManager, FileEnd


class TestFileManager(TestCase):

    def test_read_lines(self):
        file_manager = FileManager('script_test.txt')
        self.assertEqual(file_manager.next_line(), False)
        self.assertEqual(file_manager.next_line(), False)
        self.assertEqual(file_manager.next_line(), ('click', [960, 540]))
        self.assertEqual(file_manager.next_line(), ('type', 'hello world'))
        self.assertEqual(file_manager.next_line(), ('wait', 2))
        self.assertEqual(file_manager.next_line(), False)
        self.assertEqual(file_manager.next_line(), ('press', 'enter'))
        self.assertEqual(file_manager.next_line(), False)
        self.assertEqual(file_manager.next_line(), ('scroll', -10))
        self.assertEqual(file_manager.next_line(), ('scroll', 10))
        self.assertEqual(file_manager.next_line(), False)
        self.assertEqual(file_manager.next_line(), ('move', [530, 233]))
        self.assertEqual(file_manager.next_line(), False)
        self.assertEqual(file_manager.next_line(), ('right_click', [321, 423]))
        with pytest.raises(FileEnd):
            file_manager.next_line()
