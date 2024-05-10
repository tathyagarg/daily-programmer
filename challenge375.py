def carry_add(n: int) -> int:
    """
    A number is input in computer then a new no should get printed by adding one to each of its digit.
    If you encounter a 9, insert a 10 (don't carry over, just shift things around).

    For example, 998 becomes 10109.
    """
    res = ""
    for c in str(n):
        res += str(int(c) + 1)
    
    return int(res)

assert carry_add(998) == 10109
