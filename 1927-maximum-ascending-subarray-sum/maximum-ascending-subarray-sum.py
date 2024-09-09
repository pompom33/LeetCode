class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        tmp = 0
        answer = -1
        for i in range(len(nums)):
            if nums[i-1] < nums[i]:
                tmp += nums[i]
            else:
                answer = max(answer, tmp)
                tmp = 0
                tmp += nums[i]   
        answer = max(answer, tmp)         
        return answer