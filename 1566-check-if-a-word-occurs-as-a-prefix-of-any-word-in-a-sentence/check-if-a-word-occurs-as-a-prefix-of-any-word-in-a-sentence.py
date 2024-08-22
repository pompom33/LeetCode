class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        answer = -1
        splited = sentence.split()
        for i, word in enumerate(splited):
            if word.startswith(searchWord):
                answer = i+1
                break
        return answer