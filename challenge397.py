def numcompare(num1: str, num2: str) -> bool:
    """
    For the purpose of today's challenge, a Roman numeral is a non-empty string of the characters M, D, C, L, X, V, and I,
    each of which has the value 1000, 500, 100, 50, 10, 5, and 1. The characters are arranged in descending order, and the total value of the numeral
    is the sum of the values of its characters. For example, the numeral MDCCXXVIIII has the value 1000 + 500 + 2x100 + 2x10 + 5 + 4x1 = 1729.

    This challenge uses only additive notation for roman numerals. There's also subtractive notation, where 9 would be written as IX.
    You don't need to handle subtractive notation (but you can if you want to, as an optional bonus).

    Given two Roman numerals, return whether the first one is less than the second one:
    """
    char_map: dict[str, int] = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    a: int = 0
    b: int = 0

    for char in num1:
        a += char_map[char]

    for char in num2:
        b += char_map[char]

    return a < b

assert numcompare("I", "I") == False
assert numcompare("I", "II") == True
assert numcompare("II", "I") == False
assert numcompare("V", "IIII") == False
assert numcompare("MDCLXV", "MDCLXVI") == True
assert numcompare("MM", "MDCCCCLXXXXVIIII") == False

