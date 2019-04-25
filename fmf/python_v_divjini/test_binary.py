import unittest

from binary import to_binary


class TestToBinary(unittest.TestCase):
    
    def setUp(self):
        self.q = []
    
    
    def tearDown(self):
        print("here2")
    
    def test_zero(self):
        self.assertEqual(to_binary(0), '0')
        self.assertEqual(to_binary(False), '0')

        
    def test_positive(self):
        self.assertEqual(to_binary(1), '1')
        self.assertEqual(to_binary(True), '1')

        self.assertEqual(to_binary(6), '110')
        self.assertEqual(to_binary(13), '1101')
        self.assertEqual(to_binary(1024), '10000000000')

    def test_negative(self):
        self.assertEqual(to_binary(-50), '-110010')
        self.assertEqual(to_binary(-1), '-1')
        self.assertEqual(to_binary(-0), '0')

    def test_invalid(self):
        self.assertRaisesRegex(TypeError, "Only integral values are accepted", to_binary, "adsf") 

def f():
    print("Hello!")

from unittest.mock import patch
import io

class TestF(unittest.TestCase):
    
    def test_f(self):
        s = io.StringIO()
        with patch('sys.stdout', s):
            f()
        self.assertEqual(s.getvalue(), "Hello!\n")
        

if __name__ == '__main__':
    unittest.main()
