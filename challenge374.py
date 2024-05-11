def add_digits(n: int) -> int:
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

def additive_persistence(n: int) -> int:
    """
    Inspired by this tweet, today's challenge is to calculate the additive persistence of a number, defined as how many
    loops you have to do summing its digits until you get a single digit number. Take an integer N:

    Add its digits

    Repeat until the result has 1 digit

    The total number of iterations is the additive persistence of N.

    Your challenge today is to implement a function that calculates the additive persistence of a number.
    """
    i = 0
    while n > 9:
        n = add_digits(n)
        i += 1

    return i

assert additive_persistence(13) == 1
assert additive_persistence(1234) == 2
assert additive_persistence(9876) == 2
assert additive_persistence(199) == 3

