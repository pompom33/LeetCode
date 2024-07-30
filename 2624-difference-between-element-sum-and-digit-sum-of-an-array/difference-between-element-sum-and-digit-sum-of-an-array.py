class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0
        for num in nums:
            element_sum += num
            string = str(num)
            for char in string:
                digit_sum += int(char)
        answer = abs(element_sum - digit_sum)
        return answer
