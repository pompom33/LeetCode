class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        data = []
        for i, row in enumerate(mat):
            count_one = row.count(1)
            data.append([i, count_one])
        answer = sorted(data, key =lambda x:x[1], reverse=True)
        return answer[0]