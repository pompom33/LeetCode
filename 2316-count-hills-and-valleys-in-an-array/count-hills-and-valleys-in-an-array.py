class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        new_nums = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                new_nums.append(nums[i])   
        cnt = 0
        for i in range(1, len(new_nums)-1):
            if new_nums[i-1] < new_nums[i] and new_nums[i] > new_nums[i+1]:
                cnt += 1
            if new_nums[i-1] > new_nums[i] and new_nums[i] < new_nums[i+1]:
                cnt += 1
        return cnt
