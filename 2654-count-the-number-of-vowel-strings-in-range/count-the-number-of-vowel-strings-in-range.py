class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        answer = 0
        vowels = ('a', 'e', 'i', 'o', 'u')
        for i, word in enumerate(words):
            if word.startswith(vowels) and word.endswith(vowels):
                if left <= i <= right:
                    answer += 1
        return answer