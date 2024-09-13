class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        set_nums = set(nums)
        while max(set_nums) > 0:
            if 0 in set_nums:
                set_nums.remove(0)
            i = min(set_nums)
            nums = [x-i for x in set_nums]          
            cnt += 1
            set_nums = set(nums)
        return cnt
