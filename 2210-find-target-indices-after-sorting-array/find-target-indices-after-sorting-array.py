class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        answer = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] == target:
                answer.append(i)
        return answer