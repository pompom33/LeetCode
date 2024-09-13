class Solution:
    def repeatedCharacter(self, s: str) -> str:
        tmp = []
        for c in s:
            if c in tmp:
                return c
            tmp.append(c)