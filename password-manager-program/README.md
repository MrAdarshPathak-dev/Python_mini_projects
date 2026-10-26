# Password Manager Program

A small command-line password manager built as a Python mini project. It lets you save passwords for websites, view saved entries, update a password, and generate a random password.

This project is for learning and practice. It demonstrates how basic Python features can be used to build a simple, real-world-style program.

## Features

- Save a password for a website or service.
- View saved website and password entries.
- Generate an 8-character password.
- Update the password saved for an existing website.
- Store entries in `passwords.txt` so they are available the next time the program runs.

## Concepts practiced

- **Dictionaries** to associate each website with its password.
- **Loops** to keep the menu running until you choose to exit.
- **Conditionals** to handle menu choices and check whether a website exists.
- **Modules**: Python's `random` and `string` modules to generate passwords.
- **File handling** to read saved entries and write changes to `passwords.txt`.

## Run the program

Make sure Python is installed, then open a terminal in this folder and run:

```bash
python password-manager.py
```

Choose an option from the menu and follow the prompts. Password data is stored in `passwords.txt` in this folder.

## Important security note

This is a learning project, not a secure password manager. It stores passwords as plain text, without encryption. Do not use it to store real or sensitive passwords.
