# FIX: Corrected difficulty ranges so harder difficulty always means a larger number range
# (Hard was previously 1-50 which was easier than Normal's 1-100) using claude AI
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


# FIX: Added low/high parameters and range validation so out-of-range inputs are
# rejected with a warning instead of silently accepted using claude AI
def parse_guess(raw: str, low: int, high: int):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    # FIX: Validates guess is within the current difficulty's range using claude AI
    if value < low or value > high:
        return False, None, f"Please enter a number between {low} and {high}."

    return True, value, None


# FIX: Renamed parameter from 'spytecret' to 'secret' so the function uses its own
# parameter instead of a global variable, and removed the str() conversion on even
# attempts that was causing wrong hints using claude AI
def check_guess(guess, secret):
    """
    Compare guess to secret and return outcome string.

    outcome: "Win", "Too High", or "Too Low"
    """
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
