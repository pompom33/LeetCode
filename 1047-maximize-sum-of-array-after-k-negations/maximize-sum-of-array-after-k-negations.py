class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            index = nums.index(min(nums))
            nums[index] *= -1
        return sum(nums)