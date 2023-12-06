import random

def guessing_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    attempts = 0
    player_guess = None

    while player_guess != secret_number:
        try:
            player_guess = int(input("Guess the number between 1 and 10: "))
            attempts += 1

            if player_guess == secret_number:
                print(f"Congratulations! You guessed the right number in {attempts} attempts.")
            else:
                print("Wrong guess. Try again!")

                # Provide a hint
                if player_guess < secret_number:
                    print("Hint: The secret number is higher.")
                else:
                    print("Hint: The secret number is lower.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return attempts

def main():
    best_score = float('inf')

    while True:
        attempts = guessing_game()

        # Record the minimum attempts
        best_score = min(best_score, attempts)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Your best score was {best_score} attempts.")
            break

if __name__ == "__main__":
    main()
