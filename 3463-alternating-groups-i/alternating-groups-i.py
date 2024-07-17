class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        answer = 0
        length = len(colors)
        for i in range(len(colors)):
            if colors[i-1] != colors[i] and colors[(i+1) % length] != colors[i]:
                answer += 1
        return answer