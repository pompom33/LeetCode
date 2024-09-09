class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        tmp = []
        answer = []
        for i in range(len(nums)):
            if nums[i-1] < nums[i]:
                tmp.append(nums[i])
            else:
                answer.append(sum(tmp))
                tmp = []
                tmp.append(nums[i])                
        answer.append(sum(tmp))
        return max(answer)