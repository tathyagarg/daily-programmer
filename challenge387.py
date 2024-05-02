def caesar(text: str, offset: int) -> str:
    """
    Given a string of lowercase letters and a number, return a string with each letter Caesar shifted by the given amount.
    """
    result = ""
    for character in text:
        result += chr((ord(character) - 97 + offset) % 26 + 97)

    return result

def bonus1(text: str, offset: int) -> str:
    """
    Correctly handle capital letters and non-letter characters. Capital letters should also be shifted like lowercase letters, but remain capitalized.
    Leave non-letter characters, such as spaces and punctuation, unshifted.
    """
    make_character = lambda character, start: chr((ord(character) - start + offset) % 26 + start)

    result = ""
    for character in text:
        if character.isupper():
            result += make_character(character, 66)
        elif character.islower():
            result += make_character(character, 97)
        else:
            result += character

    return result


assert caesar("a", 1) == "b"
assert caesar("abcz", 1) == "bcda"
assert caesar("irk", 13) == "vex"
assert caesar("fusion", 6) == "layout"
assert caesar("dailyprogrammer", 6) == "jgorevxumxgsskx"
assert caesar("jgorevxumxgsskx", 20) == "dailyprogrammer"

assert bonus1("Daily Programmer!", 6) == "Jgore Vxumxgsskx!"
