import unittest
from unittest.mock import patch
from auto_manage_folder import SelectAction

class TestSelectAction(unittest.TestCase):
    def setUp(self):
        self.select_action = SelectAction()

    @patch('builtins.input', side_effect=['1'])
    def test_select_action_group_by_extension(self, mock_input):
        result = self.select_action.select_action()
        self.assertEqual(result, '1')

    @patch('builtins.input', side_effect=['2'])
    def test_select_action_group_by_first_letter(self, mock_input):
        result = self.select_action.select_action()
        self.assertEqual(result, '2')

    @patch('builtins.input', side_effect=['3'])
    def test_select_action_group_by_date_download(self, mock_input):
        result = self.select_action.select_action()
        self.assertEqual(result, '3')

    @patch('builtins.input', side_effect=['4'])
    def test_select_action_create_new_name(self, mock_input):
        result = self.select_action.select_action()
        self.assertEqual(result, '4')

    @patch('builtins.input', side_effect=['5'])
    def test_select_action_cut_name(self, mock_input):
        result = self.select_action.select_action()
        self.assertEqual(result, '5')

    @patch('builtins.input', side_effect=['6'])
    def test_select_action_add_text(self, mock_input):
        result = self.select_action.select_action()
        self.assertEqual(result, '6')

    @patch('builtins.input', side_effect=['7'])
    def test_select_action_auto_number(self, mock_input):
        result = self.select_action.select_action()
        self.assertEqual(result, '7')

    @patch('builtins.input', side_effect=['8'])
    def test_select_action_edit_files(self, mock_input):
        result = self.select_action.select_action()
        self.assertEqual(result, '8')

    @patch('builtins.input', side_effect=['0'])
    def test_select_action_exit(self, mock_input):
        result = self.select_action.select_action()
        self.assertEqual(result, '0')


if __name__ == '__main__':
    unittest.main()