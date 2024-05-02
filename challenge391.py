from functools import cache

@cache
def sequence(n: int) -> str:
    if n == 1: return 'a'

    return sequence(n - 1) + chr(n + 96) + sequence(n - 1)

assert sequence(1) == "a"
assert sequence(2) == "aba"
assert sequence(3) == "abacaba"
assert sequence(4) == "abacabadabacaba"
assert sequence(5) == "abacabadabacabaeabacabadabacaba"
