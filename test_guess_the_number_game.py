import unittest
from unittest.mock import patch
from random import randint
from io import StringIO
from guess_the_number_game import GuessTheNumberGame


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.results = GuessTheNumberGame()

    def test_generate_number(self):
        self.results.generate_number()
        self.assertIsNotNone(self.results.generated_number)
        self.assertTrue(1000 <= int(self.results.generated_number) <= 9999)

    def test_compare_numbers(self):
        self.results.generated_number = "1234"
        circle_count, x_count = self.results.compare_numbers("1234")
        self.assertEqual(circle_count, 4)
        self.assertEqual(x_count, 0)

        circle_count, x_count = self.results.compare_numbers("5678")
        self.assertEqual(circle_count, 0)
        self.assertEqual(x_count, 0)

        circle_count, x_count = self.results.compare_numbers("1342")
        self.assertEqual(circle_count, 1)
        self.assertEqual(x_count, 3)

        circle_count, x_count = self.results.compare_numbers("1243")
        self.assertEqual(circle_count, 2)
        self.assertEqual(x_count, 2)

    @patch("random.randint", return_value=1234)
    @patch("builtins.input", side_effect=["abcd", "123", "1235", "1234", "q"])
    def test_play(self, _, __):
        """
        Check if the play function run successfully, and the outputs and attempts are correct.
        """
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.results.generated_number = "1234"
            self.results.play()
            captured_output = captured_output.getvalue().strip().split("\n")
            expected_output1 = "Invalid input. \
                        Please enter a 4-digit number between 1000 and 9999."
            expected_output2 = "Invalid input. \
                        Please enter a 4-digit number between 1000 and 9999."
            expected_output3 = "Hints: 3 circles, 0 x's"
            expected_output4 = "Congratulations! \
                        You guessed the number in 2 attempts."
            expected_output5 = "Thanks for playing!"
            self.assertEqual(captured_output[-1], expected_output5)
            self.assertEqual(captured_output[-2], expected_output4)
            self.assertEqual(captured_output[-3], expected_output3)
            self.assertEqual(captured_output[-4], expected_output2)
            self.assertEqual(captured_output[-5], expected_output1)
            self.assertEqual(self.results.attempts, 2)


if __name__ == "__main__":
    unittest.main()
