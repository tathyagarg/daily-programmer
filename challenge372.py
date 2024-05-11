def balanced(text: str) -> bool:
    """
    Given a string containing only the characters x and y, find whether there are the same number of xs and ys.
    """
    return text.count('x') == text.count('y')

def balanced_bonus(text: str) -> bool:
    """
    Given a string containing only lowercase letters, find whether every letter that appears in the string appears the same number of times.
    Don't forget to handle the empty string ("") correctly!
    """
    if not text: return True

    count = text.count(text[0])
    for char in set(text):
        if text.count(char) != count:
            return False

    return True

assert balanced("xxxyyy") == True
assert balanced("yyyxxx") == True
assert balanced("xxxyyyy") == False
assert balanced("yyxyxxyxxyyyyxxxyxyx") == True
assert balanced("xyxxxxyyyxyxxyxxyy") == False
assert balanced("") == True
assert balanced("x") == False

assert balanced_bonus("xxxyyyzzz") == True
assert balanced_bonus("abccbaabccba") == True
assert balanced_bonus("xxxyyyzzzz") == False
assert balanced_bonus("abcdefghijklmnopqrstuvwxyz") == True
assert balanced_bonus("pqq") == False
assert balanced_bonus("fdedfdeffeddefeeeefddf") == False
assert balanced_bonus("www") == True
assert balanced_bonus("x") == True
assert balanced_bonus("") == True
