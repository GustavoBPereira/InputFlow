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
        with pytest.raises(FileEnd):
            file_manager.next_line()
