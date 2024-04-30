def can_be_sum_of(num: int, factors: list[int]) -> bool:
    possiblities: list[int] = list(filter(lambda i: i <= num, factors))
    if not possiblities: return False

    highest: int = max(possiblities)
    factors.remove(highest)

    if num == highest: return True

    return can_be_sum_of(num - highest, factors)


def practical(num: int) -> bool:
    """
    A practical number is a positive integer N such that all smaller positive integers can be represented as sums of distinct divisors of N.
    For example, 12 is a practical number because all the numbers from 1 to 11 can be expressed as sums of the divisors of 12,
    which are 1, 2, 3, 4, and 6. However, 10 is not a practical number, because 4 and 9 cannot be expressed as a sum of 1, 2, and 5.
    """

    factors = [i for i in range(1, num) if num % i == 0]

    for i in range(1, num):
        if not can_be_sum_of(i, factors.copy()):
            return False

    return True

assert practical(1) == True
assert practical(2) == True
assert practical(3) == False
assert practical(10) == False
assert practical(12) == True
