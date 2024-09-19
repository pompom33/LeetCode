class Solution:
    def checkString(self, s: str) -> bool:
        answer = True
        if "ba" in s:
            answer = False
        return answer