# Number Guessing Game

A simple Python command-line game where the player tries to guess a random number between 1 and 10.

## Overview

This project is a beginner-friendly number guessing game built in Python. The computer chooses a random number, and the player has up to 7 attempts to guess it correctly. After each guess, the game gives feedback such as "Too High!!!" or "Too low!!". If the player runs out of attempts, the game ends and reveals the correct number.

## How it works

- The program selects a random number between 1 and 10.
- The user enters a guess.
- The game checks whether the guess is valid.
- If the guess is out of range, the user is asked to enter a number from 1 to 10.
- The game compares the guess with the hidden number and gives hints.
- The player wins if they guess correctly before 7 attempts.
- The player loses if they use all 7 attempts without guessing correctly.
- After either outcome, the user is asked whether they want to play again.

## Run the game

Open a terminal in this folder and run:

```bash
python number-guessing.py
```

## Example gameplay

```text
Guess between 1 to 10: 5
Too low!!
Guess between 1 to 10: 8
Too High!!!
Guess between 1 to 10: 7
Right guess!
You won in 3 attempts :)
Do you want to play again (yes/no): yes
```

Example of a loss:

```text
Attempts limit exceeded. You lost. Right number was 9.
Do you want to play again (yes/no): no
Exited
```

## Features

- Random number generation between 1 and 10
- Input validation for non-numeric entries
- Range checking for values outside 1-10
- Hint messages: too high or too low
- Win condition after correct guess
- Lose condition after 7 attempts
- Replay option after each round

## Project files

- `number-guessing.py` — main game logic

## Learning goals

This project helps practice:

- Python loops
- conditional statements
- user input handling
- random number generation
- basic game logic and flow control
