class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count_dict = {}
        length = len(arr) 
        for i in range(length):
            count_dict[arr[i]] = count_dict.get(arr[i], 0) + 1
            if count_dict[arr[i]] > length/4:
                return arr[i]