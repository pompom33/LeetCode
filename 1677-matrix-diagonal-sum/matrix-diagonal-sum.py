class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # 1. 첫 번째 원소에서는 [0], [-1]
        # 2. 두 번째 원소에서는 [1], [-2]
        # 3. 세 번째 원소에서는 [2], [-3]
        answer = 0
        for i in range(len(mat)):
            j = -1 - i
            answer += mat[i][i] + mat[i][j]
        if len(mat) % 2 == 1:
            answer -= mat[len(mat)//2][len(mat)//2]
        return answer