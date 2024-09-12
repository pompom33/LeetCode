class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        i = 0
        arr_dict = {}
        sorted_arr = sorted(arr)
        for num in sorted_arr:
            if num not in arr_dict.keys():
                i += 1
                arr_dict[num] = i
                print("yes")
            else:
                arr_dict[num] = i
        answer = []        
        for num in arr:
            answer.append(arr_dict[num])
        return answer