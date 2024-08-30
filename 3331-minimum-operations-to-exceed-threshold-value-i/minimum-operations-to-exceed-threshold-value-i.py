class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        for num in nums:
            if num < k:
                del num
                cnt += 1
        return cnt