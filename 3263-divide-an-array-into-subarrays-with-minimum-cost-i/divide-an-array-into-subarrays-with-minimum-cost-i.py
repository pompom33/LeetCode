class Solution:
    def minimumCost(self, nums: List[int]) -> int: 
        answer = []
        for i in range(1, len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[0] + nums[i] + nums[j]
                answer.append(sum)
        return min(answer)