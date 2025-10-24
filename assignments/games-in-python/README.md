
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objetivo

Build a playable, terminal-based Hangman (forca) game in Python so students practice string manipulation, loops, conditionals, functions and basic I/O.

## 📝 Tarefas

### 🛠️ Implement the Hangman Game

#### Description
Create a command-line Hangman game that selects a secret word and lets a player guess letters until they either discover the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list (or a `words.txt` file if provided).
- Prompt the player to guess single letters and validate input (ignore empty input, non-letters, or multi-character guesses).
- Display the current progress of the word using underscores and revealed letters (example: `_ a _ _ e`).
- Track incorrect guesses and show remaining attempts (e.g., 6 attempts total).
- Do not penalize repeated guesses (previously guessed letters should be detected and reported).
- End the game with a clear win or lose message and reveal the secret word when the player loses.
- Organize the code using functions (for example: `choose_word()`, `display_progress()`, `process_guess()`, `main()`).

Example interaction (simplified):

```
Secret word: _ a _ _ _
Guess a letter: a
Correct! Word: _ a _ _ _
Incorrect guesses: 2/6
```

### 🛠️ Optional: Bonus Features

#### Description
Add one or more enhancements to make the game more polished or configurable.

#### Requirements
Completed program may also:

- Offer difficulty levels (e.g., Easy=8 attempts, Hard=4 attempts).
- Read the word list from a `words.txt` file in the same folder.
- Show simple ASCII-art hangman stages as incorrect guesses increase.
- Allow replaying multiple rounds without restarting the program.

Keep the implementation clear and well-commented so a classmate can follow your logic.
