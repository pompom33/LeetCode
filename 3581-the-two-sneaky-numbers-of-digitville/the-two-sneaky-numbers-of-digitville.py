class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [x for x, count in Counter(nums).items() if count > 1]