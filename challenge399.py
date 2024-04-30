import requests
from collections import defaultdict

def lettersum(text: str) -> int:
    """
    Assign every lowercase letter a value, from 1 for a to 26 for z.
    Given a string of lowercase letters, find the sum of the values of the letters in the string.
    """
    if text == "": return 0

    total = 0
    for char in text:
        total += ord(char) - 96

    return total

def get_words() -> list[str]:
    return requests.get("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt").text.split('\n')

def optional1() -> str:
    """
    microspectrophotometries is the only word with a letter sum of 317. Find the only word with a letter sum of 319
    """
    words = get_words()

    for word in words:
        if lettersum(word) == 319:
            return word

    return "Not found."

def optional2() -> int:
    """
    How many words have an odd letter sum?
    """
    words = get_words()
    count = 0
    for word in words:
        if lettersum(word) % 2 == 1:
            count += 1

    return count

def optional3() -> tuple[int, int]:
    """
    There are 1921 words with a letter sum of 100, making it the second most common letter sum.
    What letter sum is most common, and how many words have it?
    """
    tracker = defaultdict(lambda: 0)
    words = get_words()
    for word in words:
        tracker[lettersum(word)] += 1

    return max(tracker.items(), key=lambda pair: pair[1])

def optional4() -> tuple[str, str]:
    """
    zyzzyva and biodegradabilities have the same letter sum as each other (151), and their lengths differ by 11 letters.
    Find the other pair of words with the same letter sum whose lengths differ by 11 letters
    """
    items = defaultdict(lambda: [])
    for word in get_words():
        if word in ['zyzzyva', 'biodegradabilities']: continue

        items[lettersum(word)].append(word)

    for value in items.values():
        if (len(max(value, key=len)) - len(min(value, key=len))) >= 11:
            for i, word in enumerate(value):
                for other_word in value[i+1:]:
                    if abs(len(word) - len(other_word)) == 11:
                        return word, other_word

def optional5() -> tuple[str, str]:
    """
    cytotoxicity and unreservedness have the same letter sum as each other (188), and they have no letters in common.
    Find a pair of words that have no letters in common, and that have the same letter sum, which is larger than 188.
    There are two such pairs, and one word appears in both pairs.
    """
    items = defaultdict(lambda: [])
    for word in get_words():
        items[lettersum(word)].append(word)

    for letsum, words in items.items():
        if letsum > 188:
            for i, word in enumerate(words):
                for other_word in words[i+1:]:
                    if len(set(word) & set(other_word)) == 0:
                        return word, other_word

assert lettersum("") == 0
assert lettersum("a") == 1
assert lettersum("z") == 26
assert lettersum("cab") == 6
assert lettersum("excellent") == 100
assert lettersum("microspectrophotometries") == 317

