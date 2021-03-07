import unittest

import day_01


class Problem001Test(unittest.TestCase):
    def test_should_be_zero_floor(self):
        self.assertEqual(day_01.create_floors("(())")[-1], 0)

    def test_should_be_zero_floor_again(self):
        self.assertEqual(day_01.create_floors("()()")[-1], 0)

    def test_should_be_third_floor(self):
        self.assertEqual(day_01.create_floors("(((")[-1], 3)

    def test_should_be_third_floor_again(self):
        self.assertEqual(day_01.create_floors("(()(()(")[-1], 3)

    def test_should_be_third_floor_once_again(self):
        self.assertEqual(day_01.create_floors("))(((((")[-1], 3)

    def test_should_be_first_basement_level(self):
        self.assertEqual(day_01.create_floors("())")[-1], -1)

    def test_should_be_first_basement_level_again(self):
        self.assertEqual(day_01.create_floors("))(")[-1], -1)

    def test_should_be_third_basement_level(self):
        self.assertEqual(day_01.create_floors(")))")[-1], -3)

    def test_should_be_first_basement_level_again(self):
        self.assertEqual(day_01.create_floors(")())())")[-1], -3)

    def test_should_be_two_hundred_and_eighty_floor(self):
        self.assertEqual(day_01.create_floors(day_01.get_data())[-1], 280)

    def test_should_enter_the_basement_at_first_position(self):
        self.assertEqual(day_01.check_position(day_01.create_floors(")"), -1), 1)

    def test_should_enter_the_basement_at_fifth_position(self):
        self.assertEqual(day_01.check_position(day_01.create_floors("()())"), -1), 5)

    def test_should_enter_the_basement_at_one_thousand_seven_hundred_and_ninety_seven_position(
        self,
    ):
        self.assertEqual(
            day_01.check_position(day_01.create_floors(day_01.get_data()), -1), 1797
        )


if __name__ == "__main__":
    unittest.main()
