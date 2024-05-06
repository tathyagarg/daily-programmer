import math

def tax(amt: int) -> int:
    """
    Given a whole-number income amount up to ¤100,000,000, find the amount of tax owed in Examplania. Round down to a whole number of ¤.
    """
    tax_map = {
        10_000: 0,
        30_000: 0.1,
        100_000: 0.25,
        float('inf'): 0.4
    }

    keys = iter(tax_map.keys())

    taxed = 0
    prev = 0
    while amt:
        curr = next(keys)

        to_tax = min(amt, curr - prev)
        taxed += to_tax * tax_map[curr]

        amt -= to_tax
        prev = curr

    return math.floor(taxed)

assert tax(0) == 0
assert tax(10000) == 0
assert tax(10009) == 0
assert tax(10010) == 1
assert tax(12000) == 200
assert tax(56789) == 8697
assert tax(1234567) == 473326

