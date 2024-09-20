class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        answer = 1
        increase_cnt = 1
        decrease_cnt = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                increase_cnt += 1
                decrease_cnt = 1
                answer = max(answer, increase_cnt)
            elif nums[i-1] > nums[i]:
                increase_cnt = 1
                decrease_cnt += 1
                answer = max(answer, decrease_cnt)
            else:
                increase_cnt = 1
                decrease_cnt = 1
        return answer
            
