import unittest
from unittest.mock import patch
from io import StringIO
import getpass
import math
from badcode import OperationsManager, login_success

class OperationsManagerTest(unittest.TestCase):

    def test_perform_division(self):
        ops_manager = OperationsManager(15, 3)
        result = ops_manager.perform_division()
        self.assertEqual(result, 5)

    def test_perform_division_with_zero_b(self):
        ops_manager = OperationsManager(2, 0)
        result = ops_manager.perform_division()
        self.assertTrue(math.isnan(result))

class LoginSuccessTest(unittest.TestCase):

    @patch('builtins.input', side_effect=['10', '2', '2 + 2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_login_success(self, mock_stdout, mock_input):
        with patch.object(getpass, 'getpass', return_value='123'):
            login_success()
            self.assertEqual(mock_stdout.getvalue(), 'Login success!\n2.0\nResult: 4\n')

    @patch('builtins.input', side_effect=['root', 'wrong_password'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_login_failure(self, mock_stdout, mock_input):
        with patch.object(getpass, 'getpass', return_value='wrong_password'):
            login_success()
            self.assertEqual(mock_stdout.getvalue(), 'Wrong username or password!\n')

if __name__ == '__main__':
    unittest.main()
