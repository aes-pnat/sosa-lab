import unittest
from unittest.mock import patch
import math
from badcode import OperationsManager, login_success
import io
import builtins
import sys

def stub_stdin(testcase_inst, inputs):
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = io.StringIO(inputs)

def stub_stdouts(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = io.StringIO()
    sys.stdout = io.StringIO()
    
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

    @patch('builtins.input', side_effect=["6", "3", "1 / 0"])
    def test_invalid_expression(self, mock_input):
        expected_output = "2.0\nInvalid expression.\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            login_success()
            self.assertEqual(fake_out.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
