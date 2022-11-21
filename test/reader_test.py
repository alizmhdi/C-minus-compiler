import unittest
from scanner.reader import Reader


def close_files(reader: Reader):
    reader.close_file()


class ReaderTest(unittest.TestCase):

    def test_read_char(self):
        reader = Reader('scanner/resource/reader_test.txt')
        self.assertEqual('s', reader.read_char())
        self.assertEqual(' ', reader.read_char())
        self.assertEqual('a', reader.read_char())
        self.assertEqual('\n', reader.read_char())
        self.assertEqual('b', reader.read_char())
        self.assertEqual(None, reader.read_char())
        close_files(reader)

    def test_line_number(self):
        reader = Reader('scanner/resource/reader_test.txt')
        self.assertEqual(1, reader.get_current_line_number())
        reader.read_char()
        reader.read_char()
        reader.read_char()
        reader.read_char()
        reader.read_char()
        self.assertEqual(2, reader.get_current_line_number())
        close_files(reader)
