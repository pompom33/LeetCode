class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        answer = ""
        words = s.split()
        for i in range(k-1):
            answer += words[i]
            answer += " "
        answer += words[k-1]
        return answer

