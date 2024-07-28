import unittest
from change_file import CutNameFile

class TestCutNameFile(unittest.TestCase):
    def test_cut_name(self):
        file = CutNameFile(name="example_file", extension=".txt")

        # Test cutting name from position 1 to 6
        result = file.cut_name(1, 6)
        self.assertEqual(result, "exampl")

        # Test cutting name from position 3 to 8
        result = file.cut_name(3, 8)
        self.assertEqual(result, "ample_")

        # Test cutting name from position 5 to 10
        result = file.cut_name(5, 10)
        self.assertEqual(result, "ple_fi")

        # Test cutting name from position 2 to 2 (single character)
        result = file.cut_name(2, 2)
        self.assertEqual(result, "x")

        # Test cutting name from position 8 to 15 (out of range)
        result = file.cut_name(8, 15)
        self.assertEqual(result, "_file")

from change_file import AddNameFile

class TestAddNameFile(unittest.TestCase):
    def test_add_on_before_name(self):
        file = AddNameFile(name="example_file", extension=".txt")

        # Test adding text before the name
        result = file.add_on_before_name("prefix_")
        self.assertEqual(result, "prefix_example_file")

    def test_add_on_after_name(self):
        file = AddNameFile(name="example_file", extension=".txt")

        # Test adding text after the name
        result = file.add_on_after_name("_suffix")
        self.assertEqual(result, "example_file_suffix")

    def test_add_on_name(self):
        file = AddNameFile(name="example_file", extension=".txt")

        # Test adding text at the beginning of the name
        result = file.add_on_name("prefix_", place=1)
        self.assertEqual(result, "prefix_example_file")

        # Test adding text in the middle of the name
        result = file.add_on_name("_middle_", place=8)
        self.assertEqual(result, "example_middle__file")

        # Test adding text at the end of the name
        result = file.add_on_name("_suffix", place=13)
        self.assertEqual(result, "example_file_suffix")


from change_file import Text

class TestText(unittest.TestCase):
    def test_create_char_and_number(self):
        text = Text()
        
        # Test creating text with character 'A' and number 1
        result = text.create_char_and_number(number_start=1)
        self.assertEqual(result, '0001_')

        # Test creating text with character 'B' and number 10
        result = text.create_char_and_number(number_start=10)
        self.assertEqual(result, '0010_')

        # Test creating text with character 'C' and number 100
        result = text.create_char_and_number(number_start=100)
        self.assertEqual(result, '0100_')

        # Test creating text with character 'C', number 100, and length 3
        result = text.create_char_and_number(number_start=100, len_number=3)
        self.assertEqual(result, '100_')

        # Test creating text with character 'C', number 0, and length 3
        result = text.create_char_and_number(number_start=0, len_number=3)
        self.assertEqual(result, '001_')

    def test_create_number(self):
        text = Text()

        # Test creating text with number 1
        result = text.create_number(1)
        self.assertEqual(result, '0001')

        # Test creating text with number 10
        result = text.create_number(10)
        self.assertEqual(result, '0010')

        # Test creating text with number 100
        result = text.create_number(100)
        self.assertEqual(result, '0100')

        # Test creating text with number 100 and length 3
        result = text.create_number(100, 3)
        self.assertEqual(result, '100')

        # Test creating text with number 0
        result = text.create_number(0)
        self.assertEqual(result, '0001')

    

from change_file import RemoveNameFile

class TestRemoveNameFile(unittest.TestCase):
    def test_remove_text_in_name(self):
        file = RemoveNameFile(name="example_file", extension=".txt")

        # Test removing text at position 1 with length 3
        result = file.remove_text_in_name(vi_tri_remove_text=1, len_remove_text=3)
        self.assertEqual(result, "mple_file")

        # Test removing text at position 5 with length 2
        result = file.remove_text_in_name(vi_tri_remove_text=5, len_remove_text=2)
        self.assertEqual(result, "exame_file")

        # Test removing text at position 10 with length 4
        result = file.remove_text_in_name(vi_tri_remove_text=10, len_remove_text=4)
        self.assertEqual(result, "example_f")

        # Test removing text at position 2 with length 0
        result = file.remove_text_in_name(vi_tri_remove_text=2, len_remove_text=0)
        self.assertEqual(result, "example_file")

        # Test removing text at position 8 with length 6 (out of range)
        result = file.remove_text_in_name(vi_tri_remove_text=8, len_remove_text=6)
        self.assertEqual(result, "example")

if __name__ == '__main__':
    unittest.main()