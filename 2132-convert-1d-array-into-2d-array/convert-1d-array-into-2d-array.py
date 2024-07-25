class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        answer = []
        if m * n == len(original):
            for row in range(0, len(original), n):
                tmp = original[row: row+n]
                answer.append(tmp)
        return answer