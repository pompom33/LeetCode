class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        answer = 0
        first_index = nums.index(1)
        last_index = nums.index(len(nums))
        if first_index < last_index:
            answer = first_index + len(nums) - (last_index + 1)
        else:
            answer = first_index + len(nums) - (last_index + 1) - 1
        return answer

