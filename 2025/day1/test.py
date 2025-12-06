import unittest
import main 

class TestPart1(unittest.TestCase):

    def test_single_quater_left_rotation(self):
        result = main.solve_part1(50, ['L25'])
        self.assertEqual(result, 0)

    def test_single_half_left_rotation(self):
        result = main.solve_part1(50, ['L50'])
        self.assertEqual(result, 1)

    def test_single_full_left_rotation(self):
        result = main.solve_part1(50, ['L100'])
        self.assertEqual(result, 0)

    def test_two_full_left_rotation(self):
        result = main.solve_part1(50, ['L200'])
        self.assertEqual(result, 0)
    
    def test_single_quater_Right_rotation(self):
        result = main.solve_part1(50, ['R25'])
        self.assertEqual(result, 0)

    def test_single_half_right_rotation(self):
        result = main.solve_part1(50, ['R50'])
        self.assertEqual(result, 1)

    def test_single_full_right_rotation(self):
        result = main.solve_part1(50, ['R100'])
        self.assertEqual(result, 0)

    def test_two_full_right_rotation(self):
        result = main.solve_part1(50, ['R200'])
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
