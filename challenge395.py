def nonogramrow(items: list[int]) -> list[int]:
    """
    This challenge is inspired by nonogram puzzles, but you don't need to be familiar with these puzzles in order to complete the challenge.

    A binary array is an array consisting of only the values 0 and 1. Given a binary array of any length, return an array of positive integers
    that represent the lengths of the sets of consecutive 1's in the input array, in order from left to right.
    """
    result = []
    curr = 0

    for item in items:
        if not item and curr:
            result.append(curr)
            curr = 0

        if item:
            curr += 1

    if curr:
        result.append(curr)

    return result


assert nonogramrow([]) == []
assert nonogramrow([0,0,0,0,0]) == []
assert nonogramrow([1,1,1,1,1]) == [5]
assert nonogramrow([0,1,1,1,1,1,0,1,1,1,1]) == [5,4]
assert nonogramrow([1,1,0,1,0,0,1,1,1,0,0]) == [2,1,3]
assert nonogramrow([0,0,0,0,1,1,0,0,1,0,1,1,1]) == [2,1,3]
assert nonogramrow([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]) == [1,1,1,1,1,1,1,1]
