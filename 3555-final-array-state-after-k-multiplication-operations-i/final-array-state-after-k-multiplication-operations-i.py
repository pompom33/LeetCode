class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        operation = 1
        while operation <= k:
            for i in range(len(nums)):
                if nums[i] == min(nums):
                    nums[i] *= multiplier
                    break
                else:
                    continue
            operation += 1
        return nums
            