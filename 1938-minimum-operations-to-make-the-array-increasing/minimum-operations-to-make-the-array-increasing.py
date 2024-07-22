class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        nums2 = nums[:]
        for i in range(len(nums) - 1):
            if nums2[i] >= nums2[i+1]:
                nums2[i+1] = nums2[i] + 1
                cnt += (nums2[i+1] - nums[i+1])
        return cnt