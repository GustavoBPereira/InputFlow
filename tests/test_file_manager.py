from unittest import TestCase

from managers.file import FileManager


class TestFileManager(TestCase):

    def test_read_lines(self):
        file_manager = FileManager('script_test.txt')
        self.assertEqual(file_manager.next_line(), ['click', '960,540'])
        self.assertEqual(file_manager.next_line(), ['type', 'hello world'])
        self.assertEqual(file_manager.next_line(), ['wait', '2'])
        self.assertEqual(file_manager.next_line(), ['press', 'enter'])
        self.assertEqual(file_manager.next_line(), False)
