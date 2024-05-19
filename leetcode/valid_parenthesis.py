class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = []
        bracket_map = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in bracket_map.values():
                open_brackets.append(char)
            else:
                if not open_brackets: return False
                if bracket_map[char] != open_brackets[-1]:
                    return False
                open_brackets.pop()
        return not open_brackets
