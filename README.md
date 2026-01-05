## Number Guessing Game (CLI)

A Python command-line game where the computer selects a random number, and the player has to guess it within a limited number of attempts. The game supports multiple difficulty levels, hints, replay capability, a timer, and persistent high scores stored in JSON.

Created for https://roadmap.sh/projects/number-guessing-game

### Project Description

This project is designed as a learning exercise to practice:

- Python programming fundamentals
- Logic building with loops and conditionals
- User input validation
- Random number generation
- File handling with JSON for saving and loading data
- Modular program structure and documentation

The objective of the game is to guess the secret number (1–100) before the attempts run out.

### Game Rules

At the start of the game, current high scores are displayed.

You choose a difficulty level:

- Easy — 10 attempts
- Medium — 5 attempts
- Hard — 3 attempts

After each guess:

- If correct, the game ends and you win.
- If incorrect, you are told whether the secret number is greater or less than your guess.

Hints are provided:

- After 2 wrong guesses: a hint whether the number is even or odd.
- After 4 wrong guesses: a range-based hint. 

The game ends when:
 
- You guess correctly, or
- You run out of attempts.

At the end of the round:

- The time taken to finish the round is displayed.
- High scores are updated and saved to high_scores.json.

### Features

- Difficulty levels: Easy, Medium, Hard

- Replay option after each round

- Timer to track time spent per round

- Hint system based on number of guesses

- High score tracking per difficulty

- Persistent storage of scores in JSON

### How to Run

1. Clone the Repository
```text
git clone https://github.com/StrawThePie/number_guessing_game.git
cd number_guessing_game
```

2. (Optional) Create a Virtual Environment
```text
python -m venv .venv
```
##### On Linux/Mac

```text
source .venv/bin/activate
```
##### On Windows

```text
.venv\Scripts\activate
```

3. Run the Game

```text
python game.py
File Structure
text
number_guessing_game/
│
├── game.py             # Main game logic
├── high_scores.json    # Saved high scores (auto-created during play)
├── README.md           # Documentation
└── .gitignore          # Git ignore rules

```

### Functions Overview

- ```load_high_scores()``` Loads saved highscores from ```high_scores.json``` or creates a default record if none exists.

- ```save_high_scores(scores)``` Saves the updated high scores dictionary to ```high_scores.json```.

- ```get_hint(secret_number, attempts_taken)``` Provides hints based on the number of attempts: even/odd or a narrowed range.

- ```show_high_scores()``` Displays the current high scores at the beginning of each game round.

- ```play_game()``` Runs one round of the number guessing game, handling difficulty, guesses, hints, time tracking, and high score updates.

- ```main()``` Manages the replay loop and acts as the game entry point.

### Example Gameplay

```text
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

--- Current High Scores ---
Easy: 6 attempts
Medium: 3 attempts
Hard: No score yet
---------------------------

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2
Great! You selected Medium difficulty.
You have 5 chances to guess the correct number.

Enter your guess: 50
Incorrect! The number is greater than 50.
Enter your guess: 75
Incorrect! The number is less than 75.
Hint: The number is odd.
Enter your guess: 67
Congratulations! You guessed the correct number in 3 attempts.
Time taken: 8.30 seconds.
New High Score!
```

### Skills Learned

- Structuring projects in Python
- Using functions and modular design
- Handling user input safely
- File handling and data persistence with JSON
- Creating replayable CLI applications
- Practicing version control and documentation

Author
StrawThePie