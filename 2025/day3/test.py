import unittest
import main

class TestPart1(unittest.TestCase):

    def test_example_1(self):
        result = main.solve_part1(['987654321111111'])
        self.assertEqual(result, 98)

    def test_example_2(self):
        result = main.solve_part1(['811111111111119'])
        self.assertEqual(result, 89)

    def test_example_3(self):
        result = main.solve_part1(['234234234234278'])
        self.assertEqual(result, 78)

    def test_example_4(self):
        result = main.solve_part1(['818181911112111'])
        self.assertEqual(result, 92)

    def test_example_all(self):
        result = main.solve_part1(
            [
                '987654321111111',
                '811111111111119',
                '234234234234278',
                '818181911112111',
             ])
        self.assertEqual(result, 357)

    def test_long_1(self):
        result = main.solve_part1(['8221441533335523934234684734333842352334638213344455472314354533231333442559833436143312222328593824'])
        self.assertEqual(result, 99)

    def test_long_2(self):
        result = main.solve_part1(['2212221522112223211221222224432312222232222222422222212222222221222222621221113211114422272222622222'])
        self.assertEqual(result, 76)

    def test_long_3(self):
        result = main.solve_part1(['2312222232222222221233137252322131432221323212223322322222222322212132122221223212221222322213322111'])
        self.assertEqual(result, 75)

if __name__ == '__main__':
    unittest.main()
