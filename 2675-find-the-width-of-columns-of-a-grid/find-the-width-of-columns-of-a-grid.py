class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        answer = []
        max_num = 1
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                grid[j][i]
                max_num = max(len(str(grid[j][i])), max_num)
            answer.append(max_num)
            max_num = 1
        return answer
