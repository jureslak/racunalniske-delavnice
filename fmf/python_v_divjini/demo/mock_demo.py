import unittest
from unittest.mock import patch
import io

def f():
    print("Hello!")

class TestF(unittest.TestCase):

    def test_f(self):

        s = io.StringIO()
        with patch('sys.stdout', s):
            f()

        self.assertEquals("Hello!", s.getvalue())

if __name__ == '__main__':
    unittest.main()
