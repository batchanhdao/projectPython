import unittest
from input_type import InputAutoNumber, InputAdd, InputText, InputCut

class TestInputAutoNumber(unittest.TestCase):
    def setUp(self):
        self.input_auto_number = InputAutoNumber()

    # input is "no"
    def test_get_input_pass(self):
        print("Test input is 'no'")
        result = self.input_auto_number.get_input()
        excepted_result = {"number_start": 1, "len_number": 4}
        self.assertEqual(result, excepted_result)

    # input is "10, 6"
    def test_get_input_valid(self):
        print("Test input is '10, 6'")
        expected_result = {"number_start": 10, "len_number": 6}
        result = self.input_auto_number.get_input()
        self.assertEqual(result, expected_result)

    # input is "abc, 4"
    def test_get_input_invalid(self):
        print("Test input is 'abc, 4'")
        expected_result = {"number_start": 1, "len_number": 4}
        result = self.input_auto_number.get_input()
        self.assertEqual(result, expected_result)

    # input is len(text) != 2
    def test_get_input_no(self):
        print("Test input is '10'")
        expected_result = {"number_start": 1, "len_number": 4}
        result = self.input_auto_number.get_input()
        self.assertEqual(result, expected_result)

class TestInputAdd(unittest.TestCase):
    def setUp(self):
        self.input_add = InputAdd()

    def test_get_input_invalid(self):
        print("Test input is 'abc'")
        expected_result = 1
        result = self.input_add.get_input()
        self.assertEqual(result, expected_result)

    # input is a positive number
    def test_get_input_valid(self):
        print("Test input is '10'")
        expected_result = 10
        result = self.input_add.get_input()
        self.assertEqual(result, expected_result)

    # input is a negative number
    def test_get_input_negative(self):
        print("Test input is '-5'")
        expected_result = 1
        result = self.input_add.get_input()
        self.assertEqual(result, expected_result)

    # input is zero
    def test_get_input_zero(self):
        print("Test input is '0'")
        expected_result = 1
        result = self.input_add.get_input()
        self.assertEqual(result, expected_result)# input is not a number

class TestInputCut(unittest.TestCase):
    def setUp(self):
        self.input_cut = InputCut()

    # input is "no"
    def test_get_input_pass(self):
        print("Test input is 'no'")
        expected_result = {"bat_dau": None, "ket_thuc": None}
        result = self.input_cut.get_input()
        self.assertEqual(result, expected_result)

    # input is "1, 5"
    def test_get_input_valid(self):
        print("Test input is '1, 5'")
        expected_result = {"bat_dau": 1, "ket_thuc": 5}
        result = self.input_cut.get_input()
        self.assertEqual(result, expected_result)

    # input is "abc, 4"
    def test_get_input_invalid(self):
        print("Test input is 'abc, 4'")
        expected_result = {"bat_dau": None, "ket_thuc": None}
        result = self.input_cut.get_input()
        self.assertEqual(result, expected_result)

    # input is "10"
    def test_get_input_no(self):
        print("Test input is '10'")
        expected_result = {"bat_dau": None, "ket_thuc": None}
        result = self.input_cut.get_input()
        self.assertEqual(result, expected_result)

    # input is "5, 1"
    def test_get_input_reverse(self):
        print("Test input is '5, 1'")
        expected_result = {"bat_dau": None, "ket_thuc": None}
        result = self.input_cut.get_input()
        self.assertEqual(result, expected_result)

    # input is "1, abc"
    def test_get_input_nonnumeric(self):
        print("Test input is '1, abc'")
        expected_result = {"bat_dau": None, "ket_thuc": None}
        result = self.input_cut.get_input()
        self.assertEqual(result, expected_result)

class TestInputText(unittest.TestCase):
    def setUp(self):
        self.input_text = InputText()

    def test_get_input_pass(self):
        print("Test input is 'ex'")
        expected_result = 'ex'
        result = self.input_text.get_input("Enter some text: ")
        self.assertEqual(result, expected_result)

    def test_get_input_valid(self):
        print("Test input is 'Hello'")
        expected_result = 'Hello'
        result = self.input_text.get_input("Enter some text: ")
        self.assertEqual(result, expected_result)

    def test_get_input_empty(self):
        print("Test input is ''")
        expected_result = ''
        result = self.input_text.get_input("Enter some text: ")
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()