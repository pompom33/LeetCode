class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num
            if product > 0:
                answer = 1
            if product == 0:
                answer = 0
            if product < 0:
                answer = -1
        return answer