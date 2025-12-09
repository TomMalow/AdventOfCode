import unittest
import main

class TestPart1(unittest.TestCase):

    def test_non(self):
        result = main.solve_part1(
            [
                '...',
                '...',
                '...',
             ])
        self.assertEqual(result, 1)

    def test_single_center(self):
        result = main.solve_part1(
            [
                '@..',
                '...',
                '...',
             ])
        self.assertEqual(result, 1)


    def test_single_corner(self):
        result = main.solve_part1(
            [
                '.@.',
                '...',
                '...',
             ])
        self.assertEqual(result, 1)
 
    def test_single_side(self):
        result = main.solve_part1(
            [
                '...',
                '.@.',
                '...',
             ])
        self.assertequal(result, 1)

    def test_full_plate(self):
        result = main.solve_part1(
            [
                '@@@',
                '@@@',
                '@@@',
             ])
        self.assertequal(result, 4)


    def test_cross(self):
        result = main.solve_part1(
            [
                '@.@',
                '.@.',
                '@.@',
             ])
        self.assertequal(result, 4)

    def test_inverse_cross(self):
        result = main.solve_part1(
            [
                '.@.',
                '@.@',
                '.@.',
             ])
        self.assertequal(result, 4)

    def test_two_loines(self):
        result = main.solve_part1(
            [
                '@@@',
                '...',
                '@@@',
             ])
        self.assertequal(result, 6)

if __name__ == '__main__':
    unittest.main()
