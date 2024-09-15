class Solution:
    def specialArray(self, nums: List[int]) -> int:
        answer = -1
        x = 1
        while x <= len(nums):
            cnt = 0
            for num in nums:
                if x <= num:
                    cnt += 1
            if cnt == x:
                answer = x
                break
            x += 1
        return answer