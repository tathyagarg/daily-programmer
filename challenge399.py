def lettersum(text: str) -> int:
    """
    Assign every lowercase letter a value, from 1 for a to 26 for z.
    Given a string of lowercase letters, find the sum of the values of the letters in the string.
    """
    if text == "": return 0

    total = 0
    for char in text:
        total += ord(char) - 96

    return total

print(lettersum("microspectrophotometries"))

