class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        sorted_nums = sorted(nums)
        while len(sorted_nums) > 0:
            average = (sorted_nums[0] + sorted_nums[-1]) / 2
            averages.append(average)
            sorted_nums.pop(0)
            sorted_nums.pop()
        return min(averages)