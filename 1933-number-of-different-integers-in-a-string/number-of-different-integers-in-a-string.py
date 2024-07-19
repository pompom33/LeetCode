class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        tmp = ""
        answer = []
        for c in word:
            if c.isnumeric():
                tmp += c
            else:
                tmp += " "
        for num in tmp.split():
            answer.append(int(num))
        return len(set(answer))
