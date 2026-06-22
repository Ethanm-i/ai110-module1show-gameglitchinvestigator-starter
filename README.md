# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.

  The Glitchy Guesser is a number guessing game built with Streamlit. The player is given a secret number within a range determined by the chosen difficulty (Easy: 1–20, Normal: 1–50, Hard: 1–100) and a limited number of attempts to guess it. After each guess the game tells the player whether to go higher or lower. The score starts at 0 and increases on a win based on how few attempts were used, while wrong guesses reduce it. The goal is to guess the secret number before running out of attempts.

- [x] Detail which bugs you found.

  1. **Flipped hints** — the `check_guess` function used a parameter named `spytecret` but referenced a global variable called `secret` inside its body, so the parameter passed in was completely ignored. Combined with a `str()` conversion applied on even-numbered attempts, comparisons broke and hints ("Go Higher / Go Lower") were wrong or inverted.
  2. **Attempts counted before validation** — `st.session_state.attempts` was incremented before `parse_guess` checked whether the input was valid, so empty inputs, non-numbers, and out-of-range values all consumed an attempt.
  3. **No out-of-range warning** — `parse_guess` accepted any integer without checking whether it fell within the current difficulty's range, so a guess of 1000 on Easy (1–20) was silently processed.
  4. **Difficulty ranges were inverted** — Hard (1–50) had a smaller range than Normal (1–100), making it easier, not harder.
  5. **Attempt limits were inverted** — Easy had fewer attempts (6) than Normal (8), which is backwards.
  6. **Range not updating on difficulty change** — the info text hardcoded "1 and 100" instead of using the actual `low` and `high` values, and the secret number was never regenerated when difficulty changed.
  7. **Attempts counter and debug info lagged one click** — both were rendered before the `if submit:` block, so they always showed the state from the previous click rather than the current one.

- [x] Explain what fixes you applied.

  1. **Fixed `check_guess`** — renamed the parameter from `spytecret` to `secret` so the function uses what is passed in, and removed the even/odd `str()` conversion that was corrupting comparisons.
  2. **Fixed attempt counting** — moved `st.session_state.attempts += 1` to inside the `else` block so it only runs after `parse_guess` confirms the input is valid.
  3. **Added range validation** — added `low` and `high` parameters to `parse_guess` with a check that rejects out-of-range values and shows a descriptive error message.
  4. **Corrected difficulty ranges** — updated `get_range_for_difficulty` to Easy: 1–20, Normal: 1–50, Hard: 1–100.
  5. **Corrected attempt limits** — updated `attempt_limit_map` to Easy: 8, Normal: 6, Hard: 5.
  6. **Fixed difficulty change** — stored the current difficulty in `st.session_state` and reset the game (including a new secret within the correct range) whenever it changes; replaced the hardcoded "1 and 100" with `{low}` and `{high}`.
  7. **Fixed rendering lag** — replaced `st.info()` with an `st.empty()` placeholder filled after the submit block, and moved the debug expander to the bottom of the script so both always reflect the current click's state.
  8. **Refactored logic into `logic_utils.py`** — moved `get_range_for_difficulty`, `parse_guess`, and `check_guess` out of `app.py` so they can be imported and tested independently without needing a running Streamlit server.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Player enters there guess for example 40
2. If is not the sceret number and lower the game returns "GO Higher"
3. If the user was enters and number above the secert number the game returns "GO Lower"
4. The number of attempts and scores update
5. The Game ends when the right number is guessed or when the player runs out of attempts given.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->
![alt text](<Screenshot 2026-06-22 002439.png>) ![alt text](<Screenshot 2026-06-22 002502.png>)

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================

===================================================================================== test session starts ======================================================================================
platform win32 -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\eth\OneDrive\Desktop\codepathai\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 18 items                                                                                                                                                                              

tests\test_game_logic.py ..................                                                                                                                                               [100%]

====================================================================================== 18 passed in 0.13s ======================================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
