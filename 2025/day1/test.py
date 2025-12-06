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


class TestPart2(unittest.TestCase):

    def test_single_quater_left_rotation(self):
        result = main.solve_part2(50, ['L25'])
        self.assertEqual(result, 0)

    def test_single_half_left_rotation(self):
        result = main.solve_part2(50, ['L50'])
        self.assertEqual(result, 1)

    def test_single_full_left_rotation(self):
        result = main.solve_part2(50, ['L100'])
        self.assertEqual(result, 1)

    def test_two_full_left_rotation(self):
        result = main.solve_part2(50, ['L200'])
        self.assertEqual(result, 2)
    
    def test_single_quater_Right_rotation(self):
        result = main.solve_part2(50, ['R25'])
        self.assertEqual(result, 0)

    def test_single_half_right_rotation(self):
        result = main.solve_part2(50, ['R50'])
        self.assertEqual(result, 1)

    def test_single_full_right_rotation(self):
        result = main.solve_part2(50, ['R100'])
        self.assertEqual(result, 1)

    def test_two_full_right_rotation(self):
        result = main.solve_part2(50, ['R200'])
        self.assertEqual(result, 2)

    def test_0_to_99_left_rotation(self):
        result = main.solve_part2(0, ['L99'])
        self.assertEqual(result, 0)

    def test_0_to_100_left_rotation(self):
        result = main.solve_part2(0, ['L100'])
        self.assertEqual(result, 1)

    def test_0_to_5_left_rotation(self):
        result = main.solve_part2(0, ['L5'])
        self.assertEqual(result, 0)

    def test_1_to_5_left_rotation(self):
        result = main.solve_part2(1, ['L5'])
        self.assertEqual(result, 1)

    def test_50_to_1000_left_rotation(self):
        result = main.solve_part2(50, ['L1000'])
        self.assertEqual(result, 10)
    
    def test_50_to_1000_right_rotation(self):
        result = main.solve_part2(50, ['R1000'])
        self.assertEqual(result, 10)

    def test_0_to_100_right_rotation(self):
        result = main.solve_part2(0, ['R200'])
        self.assertEqual(result, 2)
    
    def test_0_to_105_left_rotation(self):
        result = main.solve_part2(0, ['L105'])
        self.assertEqual(result, 1)

    def test_5_to_5_left_rotation(self):
        result = main.solve_part2(5, ['L105'])
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
