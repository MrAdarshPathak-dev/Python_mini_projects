import random

number = random.randint(1, 10)
attempts = 0

while True:
    raw = input("Guess between 1 to 10: ").strip()

    if not raw.isdigit():
        print("Enter a valid number")
        continue

    guess = int(raw)

    if guess < 1 or guess > 10:
        print("Please guess in correct range!!!")
        continue

    attempts += 1

    if guess > number:
        print("Too High!!!")
        attempts += 1
    elif guess < number:
        print("Too low!!")
        attempts += 1
    else:
        print("Right guess!")
        print(f"You won in {attempts} attempts :)")

        # to play again
        while True:
            play_again = input("Do you want to play again (yes/no): ").strip().lower()
            if play_again in ("yes", "no"):  # if yes no --> break play again loop 
                break
            print("Invalid input! Type yes or no.") 

        if play_again == "no": 
            print("Exited")
            break

        print("New Game")
        number = random.randint(1, 10)
        attempts = 0