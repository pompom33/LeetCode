class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        answer = False
        single_sum = 0
        double_sum = 0
        for num in nums:
            if num < 10:
                single_sum += num
            else: 
                double_sum += num
        if single_sum != double_sum:
            answer = True
        return answer