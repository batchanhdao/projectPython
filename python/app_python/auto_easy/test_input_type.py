import unittest
from input_type import InputAutoNumber

class TestInputAutoNumber(unittest.TestCase):
    def setUp(self):
        self.input_auto_number = InputAutoNumber()

    def test_get_input_pass(self):
        result = self.input_auto_number.get_input()
        self.assertEqual(result, {"number_start": 1, "len_number": 4})

    def test_get_input_valid(self):
        user_input = "10, 6"
        expected_result = {"number_start": 10, "len_number": 6}
        with unittest.mock.patch('builtins.input', return_value=user_input):
            result = self.input_auto_number.get_input()
        self.assertEqual(result, expected_result)

    def test_get_input_invalid(self):
        user_input = "abc, def"
        expected_result = {"number_start": 1, "len_number": 4}
        with unittest.mock.patch('builtins.input', return_value=user_input):
            result = self.input_auto_number.get_input()
        self.assertEqual(result, expected_result)

    def test_get_input_no(self):
        user_input = "no"
        expected_result = {"number_start": 1, "len_number": 4}
        with unittest.mock.patch('builtins.input', return_value=user_input):
            result = self.input_auto_number.get_input()
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()