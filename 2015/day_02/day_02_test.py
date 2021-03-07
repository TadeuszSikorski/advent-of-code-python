import unittest

import day_02


class Problem001Test(unittest.TestCase):
    def test_should_be_valid_square_feet_of_wrapping_paper(self):
        self.assertEqual(
            day_02.get_surface_area_of_box(day_02.extract_dimensions("2x3x4")), 52
        )

    def test_should_be_valid_square_feet_of_slack(self):
        self.assertEqual(
            min(day_02.get_partial_calculations(day_02.extract_dimensions("2x3x4"))), 6
        )

    def test_should_be_valid_total_of_square_feet(self):
        self.assertEqual(
            day_02.get_total_of_square_feet(day_02.extract_dimensions("2x3x4")), 58
        )

    def test_should_be_valid_square_feet_of_wrapping_paper_again(self):
        self.assertEqual(
            day_02.get_surface_area_of_box(day_02.extract_dimensions("1x1x10")), 42
        )

    def test_should_be_valid_square_feet_of_slack_again(self):
        self.assertEqual(
            min(day_02.get_partial_calculations(day_02.extract_dimensions("1x1x10"))), 1
        )

    def test_should_be_valid_total_of_square_feet_again(self):
        self.assertEqual(
            day_02.get_total_of_square_feet(day_02.extract_dimensions("1x1x10")), 43
        )

    def test_should_be_valid_total_square_feet_of_wrapping_paper(self):
        self.assertEqual(
            day_02.get_total_square_feet_of_wrapping_paper(day_02.get_data()), 1586300
        )

    def test_should_be_valid_feet_of_ribbon_to_wrap_present(self):
        self.assertEqual(
            day_02.get_feet_of_ribbon_to_wrap_present(
                day_02.extract_dimensions("2x3x4")
            ),
            10,
        )

    def test_should_be_valid_feet_of_ribbon_for_bow(self):
        self.assertEqual(
            day_02.get_feet_of_ribbon_for_bow(day_02.extract_dimensions("2x3x4")), 24
        )

    def test_should_be_valid_total_of_feet(self):
        self.assertEqual(
            day_02.get_total_of_feet(day_02.extract_dimensions("2x3x4")), 34
        )

    def test_should_be_valid_feet_of_ribbon_to_wrap_present_again(self):
        self.assertEqual(
            day_02.get_feet_of_ribbon_to_wrap_present(
                day_02.extract_dimensions("1x1x10")
            ),
            4,
        )

    def test_should_be_valid_feet_of_ribbon_for_bow_again(self):
        self.assertEqual(
            day_02.get_feet_of_ribbon_for_bow(day_02.extract_dimensions("1x1x10")), 10
        )

    def test_should_be_valid_total_of_feet_again(self):
        self.assertEqual(
            day_02.get_total_of_feet(day_02.extract_dimensions("1x1x10")), 14
        )

    def test_should_be_valid_total_feet_of_ribbon(self):
        self.assertEqual(day_02.get_total_feet_of_ribbon(day_02.get_data()), 3737498)


if __name__ == "__main__":
    unittest.main()
