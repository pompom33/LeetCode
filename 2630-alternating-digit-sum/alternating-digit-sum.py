class Solution:
    def alternateDigitSum(self, n: int) -> int:
        string = str(n)
        answer = 0
        sign = 1
        for c in string:
            answer += int(c) * sign
            sign *= (-1)
        return answer