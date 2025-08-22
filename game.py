import random
import time
import json
import os

SCORES_FILE = "high_scores.json"

# ----------------------------
# High Score Management
# ----------------------------

def load_high_scores():
    """Load high scores from JSON file, or return defaults if not found."""
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r") as file:
            return json.load(file)
    return {"easy": None, "medium": None, "hard": None}


def save_high_scores(scores):
    """Save high scores to JSON file."""
    with open(SCORES_FILE, "w") as file:
        json.dump(scores, file)


# Load high scores at program start
high_scores = load_high_scores()


# ----------------------------
# Game Helper Functions
# ----------------------------

def get_hint(secret_number, attempts_taken):
    """Provide hints based on attempt number and secret number."""
    if attempts_taken == 2:
        return "Hint: The number is even." if secret_number % 2 == 0 else "Hint: The number is odd."
    elif attempts_taken == 4:
        low = max(1, secret_number - 10)
        high = min(100, secret_number + 10)
        return f"Hint: The number is between {low} and {high}."
    return None


def show_high_scores():
    """Display current high scores if any exist."""
    print("\n--- Current High Scores ---")
    for level, score in high_scores.items():
        if score is not None:
            print(f"{level.capitalize()}: {score} attempts")
        else:
            print(f"{level.capitalize()}: No score yet")
    print("---------------------------\n")


# ----------------------------
# Core Game Function
# ----------------------------

def play_game():
    """Play one round of the guessing game."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Your goal is to guess the correct number within the allowed chances.\n")

    # Show current high scores before starting
    show_high_scores()

    secret_number = random.randint(1, 100)

    # Difficulty selection
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        attempts_allowed = 10
        difficulty_key = "easy"
        print("Great! You selected Easy difficulty.")
    elif choice == "2":
        attempts_allowed = 5
        difficulty_key = "medium"
        print("Great! You selected Medium difficulty.")
    elif choice == "3":
        attempts_allowed = 3
        difficulty_key = "hard"
        print("Great! You selected Hard difficulty.")
    else:
        attempts_allowed = 5
        difficulty_key = "medium"
        print("Invalid choice. Defaulting to Medium difficulty.")

    print(f"You have {attempts_allowed} chances to guess the correct number.")

    start_time = time.time()
    attempts_taken = 0

    # Guessing loop
    while attempts_taken < attempts_allowed:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts_taken += 1

        if guess == secret_number:
            end_time = time.time()
            total_time = end_time - start_time
            print(f"Congratulations! You guessed the correct number in {attempts_taken} attempts.")
            print(f"Time taken: {total_time:.2f} seconds.")

            # High score update
            best_score = high_scores[difficulty_key]
            if best_score is None or attempts_taken < best_score:
                high_scores[difficulty_key] = attempts_taken
                save_high_scores(high_scores)
                print("New High Score!")
            else:
                print(f"Current High Score for {difficulty_key.capitalize()}: {best_score} attempts.")
            return

        elif guess < secret_number:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Incorrect! The number is less than {guess}.")

        # Give hint if available
        hint = get_hint(secret_number, attempts_taken)
        if hint:
            print(hint)

    # Loss case
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Sorry, you've run out of chances. The correct number was {secret_number}.")
    print(f"Time taken: {total_time:.2f} seconds.")

    # Show high score reminder
    best_score = high_scores[difficulty_key]
    if best_score:
        print(f"High Score for {difficulty_key.capitalize()}: {best_score} attempts.")
    else:
        print(f"No High Score yet for {difficulty_key.capitalize()}.")


# ----------------------------
# Game Entry Point
# ----------------------------

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
