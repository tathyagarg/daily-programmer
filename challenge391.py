from functools import cache

@cache
def sequence(n: int) -> str:
    """
    The ABACABA sequence is defined as follows: the first iteration is the first letter of the alphabet (a).
    To form the second iteration, you take the second letter (b) and put the first iteration (just a in this case) before and after it, to get aba.
    For each subsequent iteration, place a copy of the previous iteration on either side of the next letter of the alphabet.
    """
    if n == 1: return 'a'

    return sequence(n - 1) + chr(n + 96) + sequence(n - 1)

assert sequence(1) == "a"
assert sequence(2) == "aba"
assert sequence(3) == "abacaba"
assert sequence(4) == "abacabadabacaba"
assert sequence(5) == "abacabadabacabaeabacabadabacaba"
