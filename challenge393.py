def change(amount: int) -> int:
    """
    The country of Examplania has coins that are worth 1, 5, 10, 25, 100, and 500 currency units.
    At the Zeroth Bank of Examplania, you are trained to make various amounts of money by using as many ¤500 coins as possible,
    then as many ¤100 coinsas possible, and so on down.

    For instance, if you want to give someone ¤468, you would give them four ¤100 coins, two ¤25 coins, one ¤10 coin, one ¤5 coin,
    and three ¤1 coins, for a total of 11 coins.

    Write a function to return the number of coins you use to make a given amount of change.
    """
    coins: list[int] = [1, 5, 10, 25, 100, 500]
    count: int = 0

    while amount:
        use = max(list(filter(lambda i: i <= amount, coins)))
        amount -= use

        count += 1

    return count

assert change(0) == 0
assert change(12) == 3
assert change(468) == 11
assert change(123456) == 254
