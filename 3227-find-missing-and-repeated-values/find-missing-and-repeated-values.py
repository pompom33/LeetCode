class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        cnt_dict = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                key = grid[i][j]
                cnt_dict[key] = cnt_dict.get(key, 0) + 1
                if cnt_dict[key] == 2:
                    repeating = key
        for i in range(1,len(grid[0])**2+1):
            if i not in cnt_dict.keys():
                missing = i
                break
        return [repeating, missing]