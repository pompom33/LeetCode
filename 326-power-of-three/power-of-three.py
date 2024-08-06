class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        answer = False
        while True:
            if n == 1:
                answer = True
                break
            elif n < 3:
                break
            n /= 3
        return answer