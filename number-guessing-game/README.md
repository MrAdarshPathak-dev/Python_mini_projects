# Number Guessing Game

A simple Python command-line game where the player tries to guess a random number between 1 and 10.

## How it works

- The program selects a random number between 1 and 10.
- The user enters a guess.
- The game tells the player whether the guess is too high, too low, or correct.
- The program tracks the number of attempts.
- After a correct guess, the player can choose to play again.

## Run the game

Open a terminal in this folder and run:

```bash
python number-guessing.py
```

## Example

```text
Guess between 1 to 10: 5
Too low!!
Guess between 1 to 10: 8
Too High!!!
Guess between 1 to 10: 7
Right guess!
You won in 3 attempts :)
```

## Features

- Input validation for non-numeric entries
- Range checking for values outside 1-10
- Feedback after every guess
- Replay option after each win

## Project files

- `number-guessing.py` — main game logic
