class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        answer = 0
        for i in range(len(arr1)):
            flag = True
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    flag = False
                    continue  
            if flag:
                answer += 1    
        return answer
