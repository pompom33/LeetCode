class Solution:
    def sumZero(self, n: int) -> List[int]:
        nums = [x+1 for x in range(n-1)]
        nums.append(sum(nums) * -1)
        return nums