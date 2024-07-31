class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        answer = float('inf')
        for i in range(1, len(nums)):
            for j in range(i+1, len(nums)):
                sum_ = nums[0] + nums[i] + nums[j]
                answer = min(sum_, answer)
        return answer