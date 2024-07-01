class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count_dict = {}
        answer = []
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        sorted_dict = sorted(count_dict.items(), key=lambda x: (x[1], -x[0]))
        for key, value in sorted_dict:
            answer.extend([key]*value)
        return answer