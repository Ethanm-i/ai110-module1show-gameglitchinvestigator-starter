from logic_utils import check_guess, parse_guess, get_range_for_difficulty


# ---------------------------------------------------------------------------
# check_guess — fixes: flipped hints, spytecret parameter bug
# ---------------------------------------------------------------------------

def test_winning_guess():
    # Guess matches secret → Win
    assert check_guess(50, 50) == "Win"

def test_guess_too_high():
    # Guess ABOVE secret → "Too High" (hints were previously flipped)
    assert check_guess(60, 50) == "Too High"

def test_guess_too_low():
    # Guess BELOW secret → "Too Low" (hints were previously flipped)
    assert check_guess(40, 50) == "Too Low"

def test_check_guess_uses_parameter_not_global():
    # Before fix, check_guess used a global 'secret' instead of its parameter.
    # These two calls with different secrets must return different outcomes.
    assert check_guess(10, 5) == "Too High"
    assert check_guess(10, 50) == "Too Low"


# ---------------------------------------------------------------------------
# get_range_for_difficulty — fix: Hard had smaller range than Normal
# ---------------------------------------------------------------------------

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_difficulty_ranges_increase_with_difficulty():
    # Harder difficulty must mean a larger number range
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high


# ---------------------------------------------------------------------------
# parse_guess — fixes: no range warning, invalid inputs counting as attempts
# ---------------------------------------------------------------------------

def test_valid_guess_in_range():
    ok, value, err = parse_guess("42", 1, 100)
    assert ok is True
    assert value == 42
    assert err is None

def test_boundary_low_is_valid():
    ok, value, _ = parse_guess("1", 1, 100)
    assert ok is True
    assert value == 1

def test_boundary_high_is_valid():
    ok, value, _ = parse_guess("100", 1, 100)
    assert ok is True
    assert value == 100

def test_empty_string_rejected():
    # Empty input must NOT count as an attempt (ok=False prevents incrementing)
    ok, value, err = parse_guess("", 1, 100)
    assert ok is False
    assert value is None
    assert err is not None

def test_none_input_rejected():
    ok, value, _ = parse_guess(None, 1, 100)
    assert ok is False
    assert value is None

def test_non_number_rejected():
    ok, value, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert value is None
    assert err is not None

def test_out_of_range_high_rejected():
    # 1000 is above the range — must be rejected with a warning message
    ok, value, err = parse_guess("1000", 1, 100)
    assert ok is False
    assert value is None
    assert err is not None

def test_out_of_range_low_rejected():
    # -5 is below the range — must be rejected with a warning message
    ok, value, err = parse_guess("-5", 1, 100)
    assert ok is False
    assert value is None
    assert err is not None

def test_range_error_message_mentions_bounds():
    # Error message should tell the player the valid range
    _, _, err = parse_guess("999", 1, 100)
    assert "1" in err and "100" in err

def test_decimal_input_parsed_as_int():
    # Decimal inputs like "7.9" should be accepted and truncated to int
    ok, value, _ = parse_guess("7.9", 1, 100)
    assert ok is True
    assert value == 7
