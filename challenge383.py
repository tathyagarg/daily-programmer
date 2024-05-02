def same_necklace(a: str, b: str) -> bool:
    """
    Imagine a necklace with lettered beads that can slide along the string. Here's an example image.
    In this example, you could take the N off NICOLE and slide it around to the other end to make ICOLEN.
    Do it again to get COLENI, and so on.
    For the purpose of today's challenge, we'll say that the strings "nicole", "icolen", and "coleni"describe the same necklace.

    Generally, two strings describe the same necklace if you can remove some number of letters from the beginning of one,
    attach them to the end in their original ordering, and get the other string. Reordering the letters in some other way does not, in general,
    produce a string that describes the same necklace.

    Write a function that returns whether two strings describe the same necklace.
    """
    if len(a) != len(b): return False
    if a == b: return True

    for _ in range(1, len(a)):
        b = b[1:] + b[:1]
        if a == b:
            return True

    return False

def repeats(text: str) -> int:
    """
    """
    if text == "": return True

    count = 0
    for i in range(1, len(text)+1):
        new = text[i:] + text[:i]
        count += text == new

    return count

assert same_necklace("nicole", "icolen") == True
assert same_necklace("nicole", "lenico") == True
assert same_necklace("nicole", "coneli") == False
assert same_necklace("aabaaaaabaab", "aabaabaabaaa") == True
assert same_necklace("abc", "cba") == False
assert same_necklace("xxyyy", "xxxyy") == False
assert same_necklace("xyxxz", "xxyxz") == False
assert same_necklace("x", "x") == True
assert same_necklace("x", "xx") == False
assert same_necklace("x", "") == False
assert same_necklace("", "") == True

assert repeats("abc") == 1
assert repeats("abcabcabc") == 3
assert repeats("abcabcabcx") == 1
assert repeats("aaaaaa") == 6
assert repeats("a") == 1
assert repeats("") == 1