class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        answer = 0
        for i in range(len(colors)):
            if colors[i-2] != colors[i-1] and colors[i-1] != colors[i]:
                answer += 1
        return answer