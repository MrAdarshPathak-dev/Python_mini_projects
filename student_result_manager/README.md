# Student Manager CLI

A beginner-friendly, menu-driven Python command-line app for storing student marks and checking pass/fail results.

## Features

- Add a student with their marks.
- View all students and marks currently in the app.
- Look up a student by name and check their result.
- Reject names made up only of digits and marks outside the 0–100 range.
- Mark students with 40 or more as **PASS**; marks below 40 are **FAIL**.

## Requirements

- Python 3.x

## Run

From this project folder, run:

```bash
python app.py
```

On Windows, you can also use the Python launcher:

```bash
py app.py
```

Choose an option from the menu and follow the prompts. Select **4** to exit the app.

## Data storage

Student records are kept in memory and are cleared when the app exits. If you add a student using a name that already exists, the new marks replace the previous marks for that name.
