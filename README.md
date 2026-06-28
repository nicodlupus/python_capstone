# Python Capstone

A collection of Python projects organized by difficulty, built while learning Python.

## Structure

```
python_capstone/
└── beginner_level/
    └── guess_the_number.py
```

## Projects

### Beginner Level

#### 🎯 Guess the Number

A console number-guessing game. The program picks a random number within a range
you choose, and you try to guess it within 10 chances — with optional hints along the way.

**Features**
- You set the lowest and highest numbers of the range.
- 10 chances to guess the secret number.
- Higher / lower feedback after each guess.
- A built-in hint system:
  - **Even or odd** — revealed automatically before you start.
  - **Divisible by 10?** — offered after your 1st guess (if you want it).
  - **Divisible by 3 (if odd) or 4 (if even)?** — offered after your 2nd guess (if you want it).

**How to run**
```bash
cd beginner_level
python guess_the_number.py
```

## Requirements

- Python 3.x (uses only the standard library — no extra packages needed).

## Author

[nicodlupus](https://github.com/nicodlupus)
