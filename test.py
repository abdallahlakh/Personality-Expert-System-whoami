import unittest
from unittest.mock import patch
from forr import main

class TestPersonalityType(unittest.TestCase):
    @patch('builtins.input', side_effect=['John', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no'])
    def test_main(self, input):
        with patch('builtins.print') as p:
            main()
            output = p.call_args_list
            self.assertEqual(output[-10][0][0], 'Is John a Alpha?')
            self.assertEqual(output[-9][0][0], 'Is John a Beta?')
            self.assertEqual(output[-8][0][0], 'Is John a Sigma?')
            self.assertEqual(output[-7][0][0], 'Is John a Omega?')
            self.assertEqual(output[-6][0][0], 'Is John a Gamma?')
            self.assertEqual(output[-5][0][0], 'Is John a Delta?')
            self.assertEqual(output[-4][0][0], 'Is John a Epsilon?')
            self.assertEqual(output[-3][0][0], 'Is John a Zeta?')
            self.assertEqual(output[-2][0][0], 'Is John a Theta?')
            self.assertEqual(output[-1][0][0], 'Is John a Iota?')

if __name__ == '__main__':
    unittest.main()