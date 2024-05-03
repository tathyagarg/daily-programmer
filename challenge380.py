import requests
from collections import defaultdict

def smorse(text: str) -> str:
    """
    For the purpose of this challenge, Morse code represents every letter as a sequence of 1-4 characters, each of which is either
    . (dot) or - (dash). The code for the letter a is .-, for b is -..., etc. The codes for each letter a through z are:
    """
    encoding_map = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..'
    }

    return ''.join(map(encoding_map.get, text))


def get_words() -> list[str]:
    words = requests.get('https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt').text
    return words.split()


def bonus1() -> str:
    """
    The sequence -...-....-.--. is the code for four different words (needing, nervate, niding, tiling).
    Find the only sequence that's the code for 13 different words.
    """
    count_map = defaultdict(int)
    for word in get_words():
        encoding = smorse(word)

        count_map[encoding] += 1
        if count_map[encoding] == 13:
            return encoding


def bonus2() -> str:
    """
    autotomous encodes to .-..--------------..-..., which has 14 dashes in a row. Find the only word that has 15 dashes in a row.
    """
    for word in get_words():
        if '-'*15 in smorse(word):
            return word


def bonus3() -> str:
    """
    Call a word perfectly balanced if its code has the same number of dots as dashes.
    counterdemonstrations is one of two 21-letter words that's perfectly balanced. Find the other one.
    """
    for word in get_words():
        if len(word) != 21: continue
        if word == 'counterdemonstrations': continue

        encoding = smorse(word)
        dot_count, dash_count = encoding.count('.'), encoding.count('-')

        if dot_count == dash_count:
            return word


def bonus4() -> str:
    """
    protectorate is 12 letters long and encodes to .--..-.----.-.-.----.-..--., which is a palindrome (i.e. the string is the same when reversed).
    Find the only 13-letter word that encodes to a palindrome.
    """
    for word in get_words():
        if len(word) != 13: continue

        encoding = smorse(word)
        if encoding == encoding[::-1]: return word


assert smorse("sos") == "...---..."
assert smorse("daily") == "-...-...-..-.--"
assert smorse("programmer") == ".--..-.-----..-..-----..-."
assert smorse("bits") == "-.....-..."
assert smorse("three") == "-.....-..."

assert bonus1() == '-....--....'
assert bonus2() == 'bottommost'
assert bonus3() == 'overcommercialization'
assert bonus4() == 'intransigence'


