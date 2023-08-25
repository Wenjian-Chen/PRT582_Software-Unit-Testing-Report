"""This module is a simple Guess the Number game where the player needs to"""
import random


class GuessTheNumberGame:
    """
    A simple Guess the Number game where the player needs to\
        guess a randomly generated 4-digit number.
    
    The game provides hints to the player \
        about the accuracy of their guess using 'circle' and 'x' symbols.
    'circle' indicates that one digit is correct and in the right spot,\
        while 'x' indicates a correct digit in the wrong spot.
    
    Attributes:
        generated_number (str): The randomly generated 4-digit number.
        attempts (int): The number of attempts taken to guess the correct number.
    """

    def __init__(self):
        """Initialize the game with attributes."""
        self.generated_number = None  # The randomly generated 4-digit number
        self.attempts = 0  # Counter to keep track of the number of attempts

    def generate_number(self):
        """
        Generate a random 4-digit number.

        This function generates a random 4-digit number between 1000 and 9999\
            and assigns it to the `generated_number` attribute of the class.
        """
        self.generated_number = str(random.randint(1000, 9999))
    def compare_numbers(self, guess):
        """
        Compare the user's guess with the generated number and provide hints.

        Args:
            guess (str): The user's guess (4-digit number).

        Returns:
            The number of correct digits in the correct spot (circle_count)\
                and the number of correct digits in the wrong spot (x_count).
        """
        # Initialize counts
        circle_count = 0  # Count of correct digits in the correct spot
        x_count = 0  # Count of correct digits in the wrong spot

        # Iterate over each digit in the guess
        for i in range(4):
            # Check if the digit is in the correct spot
            if guess[i] == self.generated_number[i]:
                circle_count += 1
            # Check if the digit is in the wrong spot
            elif guess[i] in self.generated_number:
                x_count += 1

        # Return the counts
        return circle_count, x_count

    def play(self):
        """Play the Guess the Number game."""
        self.generate_number()  # Generate a new random number

        while True:
            guess = input("Enter your guess (4 digits) or 'q' to quit: ")
            # Check if user wants to quit
            if guess.lower() == "q":
                break

            # Check if input is valid
            if len(guess) != 4 or not guess.isdigit() or int(guess) < 1000:
                print(
                    "Invalid input. \
                        Please enter a 4-digit number between 1000 and 9999."
                )
                continue

            # Update attempts count
            self.attempts += 1

            # Compare user's guess with the generated number
            circle_count, x_count = self.compare_numbers(guess)

            # Check if user guessed the number
            if circle_count == 4:
                print(
                    f"Congratulations! \
                        You guessed the number in {self.attempts} attempts."
                )
                replay = input("Do you want to play again? (y/n): ")

                # Check if user wants to play again
                if replay.lower() == "y":
                    self.attempts = 0
                    self.generate_number()  # Generate a new random number
                else:
                    print("Thanks for playing!")
                    break  # Quit the game
            else:
                # Print hints
                print(f"Hints: {circle_count} circles, {x_count} x's")


if __name__ == "__main__":
    game = GuessTheNumberGame()
    game.play()  # Start the game
