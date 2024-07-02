class Solution:
    def countAsterisks(self, s: str) -> int:
        answer = 0
        s_split = s.split("|")
        for i in range(len(s_split)):
            if i % 2 == 0:
                count_dict = Counter(s_split[i])
                answer += count_dict["*"]
        return answer 