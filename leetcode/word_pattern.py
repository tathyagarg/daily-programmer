class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(s.split()) != len(pattern): return False

        word_map = {}
        rev = {}
        for char, word in zip(pattern, s.split()):
            if (word in word_map and word_map[word] != char) or (char in rev and rev[char] != word):
                return False

            word_map[word] = char
            rev[char] = word
        return True