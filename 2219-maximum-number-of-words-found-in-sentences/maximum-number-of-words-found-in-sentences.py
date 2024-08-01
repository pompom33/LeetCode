class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer = float("-inf")
        for sentence in sentences:
            answer = max(answer, len(sentence.split()))
        return answer
            