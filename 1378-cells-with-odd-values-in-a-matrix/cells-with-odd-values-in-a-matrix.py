class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        cnt = 0
        initial_matrix = [[0 for x in range(n)] for y in range(m)]
        for row, col in indices:
            for i in range(n):
                initial_matrix[row][i] += 1
            for i in range(m):
                initial_matrix[i][col] += 1
        for i in range(m):
            for j in range(n):
                if initial_matrix[i][j] % 2 == 1:
                    cnt += 1
        return cnt

        