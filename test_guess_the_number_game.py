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
        self.assertTrue(
            1000 <= int(self.results.generated_number) <= 9999
            and len(self.results.generated_number) == 4
            and self.results.generated_number.isdigit()
        )

    def test_compare_numbers(self):
        self.results.generated_number = "1234"
        Hints = self.results.compare_numbers("1234")
        self.assertEqual(Hints, "OOOO")

        Hints = self.results.compare_numbers("5678")
        self.assertEqual(Hints, "____")

        Hints = self.results.compare_numbers("1342")
        self.assertEqual(Hints, "OXXX")

        Hints = self.results.compare_numbers("1243")
        self.assertEqual(Hints, "OOXX")

    @patch("random.randint", return_value=1234)
    @patch("builtins.input", side_effect=["abcd", "123", "1235", "1234", "q"])
    def test_play(self, _, __):
        """
        Check if the play function run successfully, and the outputs and attempts are correct.
        """
        with patch("sys.stdout", new=StringIO()) as captured_output:
            with self.assertRaises(SystemExit):
                self.results.play()
                captured_output = captured_output.getvalue().strip().split("\n")
                expected_output1 = "Invalid input. \
                            Please enter a 4-digit number between 1000 and 9999."
                expected_output2 = "Invalid input. \
                            Please enter a 4-digit number between 1000 and 9999."
                expected_output3 = "Hints: OOO_"
                expected_output4 = "Congratulations! \
                            You guessed the number in 2 attempts."
                self.assertEqual(captured_output[-1], expected_output4)
                self.assertEqual(captured_output[-2], expected_output3)
                self.assertEqual(captured_output[-3], expected_output2)
                self.assertEqual(captured_output[-4], expected_output1)
                self.assertEqual(self.results.attempts, 2)

    @patch("random.randint", return_value=1234)
    @patch("builtins.input", side_effect=["1234", "y", "2143", "1234", "q"])
    def test_play_replay(self, _, __):
        """
        Check if replay successfully by check the attempts
        """
        with self.assertRaises(SystemExit):
            self.results.play()
            self.assertEqual(self.results.attempts, 2)


if __name__ == "__main__":
    unittest.main()
