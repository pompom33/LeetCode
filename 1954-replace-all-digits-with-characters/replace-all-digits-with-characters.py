class Solution:
    def replaceDigits(self, s: str) -> str:
        listed = list(s)
        for i in range(1, len(s), 2):
            listed[i] = chr(ord(listed[i-1]) + int(listed[i]))
        return "".join(listed)