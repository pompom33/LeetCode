# 1. mat를 순회하며 1의 개수를 센다
# 2. 1의 개수가 가장 많은 원소를 구한다 = am
# 3. 그 원소를 반환한다

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        tmp = []
        for i in range(len(mat)):
            count_one = mat[i].count(1)
            tmp.append(count_one)
        for j in range(len(tmp)):
            if max(tmp) == tmp[j]:
                return [j, max(tmp)]