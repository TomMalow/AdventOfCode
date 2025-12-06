import unittest
import main

class TestPart1(unittest.TestCase):

    def test_11_22(self):
        result = main.solve_part1([[11, 22]])
        self.assertEqual(result, 33)

    def test_95_115(self):
        result = main.solve_part1([[95, 115]])
        self.assertEqual(result, 99)

    def test_998_1012(self):
        result = main.solve_part1([[998, 1012]])
        self.assertEqual(result, 1010)

    def test_1188511880_1188511890(self):
        result = main.solve_part1([[1188511880, 1188511890]])
        self.assertEqual(result, 1188511885)

    def test_222220_222224(self):
        result = main.solve_part1([[222220, 222224]])
        self.assertEqual(result, 222222)

    def test_1698522_1698528(self):
        result = main.solve_part1([[1698522, 1698528]])
        self.assertEqual(result, 0)

    def test_446443_446449(self):
        result = main.solve_part1([[446443, 446449]])
        self.assertEqual(result, 446446)

    def test_38593856_38593862(self):
        result = main.solve_part1([[38593856, 38593862]])
        self.assertEqual(result, 38593859)

class TestPart2(unittest.TestCase):

    def test_11_22(self):
        result = main.solve_part2([[11, 22]])
        self.assertEqual(result, 11 + 22)

    def test_95_115(self):
        result = main.solve_part2([[95, 115]])
        self.assertEqual(result, 99 + 111)

    def test_998_1012(self):
        result = main.solve_part2([[998, 1012]])
        self.assertEqual(result, 999 + 1010)

    def test_1188511880_1188511890(self):
        result = main.solve_part2([[1188511880, 1188511890]])
        self.assertEqual(result, 1188511885)

    def test_222220_222224(self):
        result = main.solve_part2([[222220, 222224]])
        self.assertEqual(result, 222222)

    def test_1698522_1698528(self):
        result = main.solve_part2([[1698522, 1698528]])
        self.assertEqual(result, 0)

    def test_446443_446449(self):
        result = main.solve_part2([[446443, 446449]])
        self.assertEqual(result, 446446)

    def test_38593856_38593862(self):
        result = main.solve_part2([[38593856, 38593862]])
        self.assertEqual(result, 38593859)

    def test_565653_565659(self):
        result = main.solve_part2([[565653, 565659]])
        self.assertEqual(result, 565656)

    def test_824824821_824824827(self):
        result = main.solve_part2([[824824821, 824824827]])
        self.assertEqual(result, 824824824)

    def test_2121212118_2121212124(self):
        result = main.solve_part2([[2121212118, 2121212124]])
        self.assertEqual(result, 2121212121)

if __name__ == '__main__':
    unittest.main()
