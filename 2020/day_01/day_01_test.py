import unittest

import day_01


class Problem001Test(unittest.TestCase):
    def test_should_be_valid_product_of_two_entries_that_sum_to_2020_from_example(self):
        self.assertEqual(
            day_01.get_product_of_two_entries_that_sum_to_2020(
                [1721, 979, 366, 299, 675, 1456]
            ),
            514579,
        )

    def test_should_be_valid_product_of_three_entries_that_sum_to_2020_from_example(
        self,
    ):
        self.assertEqual(
            day_01.get_product_of_three_entries_that_sum_to_2020(
                [1721, 979, 366, 299, 675, 1456]
            ),
            241861950,
        )

    def test_should_be_valid_product_of_two_entries_that_sum_to_2020(self):
        self.assertEqual(
            day_01.get_product_of_two_entries_that_sum_to_2020(day_01.get_data()),
            1010299,
        )

    def test_should_be_valid_product_of_three_entries_that_sum_to_2020(self,):
        self.assertEqual(
            day_01.get_product_of_three_entries_that_sum_to_2020(day_01.get_data()),
            42140160,
        )


if __name__ == "__main__":
    unittest.main()
