# -*- coding: utf8 -*-

from tictactoe import ioutil
import unittest
from unittest import mock


class TestIO(unittest.TestCase):

    @mock.patch('builtins.input', return_value=' Ćrt\n9え')
    def test_get_player_name(self, mock_input):
        self.assertEqual(ioutil.get_player_name(1), ' Ćrt\n9え')

        # brute force way: (don't do this)
        ioutil.input = lambda *args: 'Luke'
        self.assertEqual(ioutil.get_player_name(1), 'Luke')
        ioutil.input = input

    # a different (possibly better) approach
    def test_get_player_symbol(self):
        input_mock = mock.Mock(side_effect=['banana', 'x'])
        self.assertEqual(ioutil.get_player_symbol(input_mock, 1), 'x')

        input_mock = mock.Mock(side_effect=['x'])
        self.assertEqual(ioutil.get_player_symbol(input_mock, 1), 'x')

        input_mock = mock.Mock(side_effect=['garbage', '  ', '9 ', '\n\n', 'え'])
        self.assertEqual(ioutil.get_player_symbol(input_mock, 1), 'え')

    def test_get_player_symbol(self):
        input_mock = mock.Mock(side_effect=['banana', 'x'])
        self.assertEqual(ioutil.get_player_symbol(input_mock, 1), 'x')

        input_mock = mock.Mock(side_effect=['x'])
        self.assertEqual(ioutil.get_player_symbol(input_mock, 1), 'x')

        input_mock = mock.Mock(side_effect=['garbage', '  ', '9 ', '\n\n', 'え'])
        self.assertEqual(ioutil.get_player_symbol(input_mock, 1), 'え')

    def test_get_int(self):
        input_seq = ['as', 'one', '3.14', 'r112', ' 34 ']
        with mock.patch('builtins.input', side_effect=input_seq):
            self.assertEqual(ioutil.get_int(''), 34)

        input_seq = ['\n42  \t']
        with mock.patch('builtins.input', side_effect=input_seq):
            self.assertEqual(ioutil.get_int(''), 42)

    def test_get_bool(self):
        input_seq = ['as', 'ye', ' y', 'y']
        with mock.patch('builtins.input', side_effect=input_seq):
            self.assertTrue(ioutil.get_bool(''))

        input_seq = ['', 'Nope', 'y', 'banana', 'ananas']
        with mock.patch('builtins.input', side_effect=input_seq):
            self.assertTrue(ioutil.get_bool('', accepted=['banana']))

        input_seq = ['', 'N', 'yup', 'banana', 'ananas', 'pehta']
        with mock.patch('builtins.input', side_effect=input_seq):
            self.assertFalse(ioutil.get_bool('', rejected=['ananas']))

        input_seq = ['', 'N', 'yup', 'banana', 'ananas', 'pehta']
        with mock.patch('builtins.input', side_effect=input_seq):
            self.assertFalse(ioutil.get_bool('', rejected=['ananas', '']))

        input_seq = ['']
        with mock.patch('builtins.input', side_effect=input_seq):
            self.assertTrue(ioutil.get_bool('', accepted=['']))

if __name__ == '__main__':
    unittest.main()
