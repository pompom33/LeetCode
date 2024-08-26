class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dict = {}
        answer = []
        for item in items1:
            dict[item[0]] = dict.get(item[0], 0) + item[1]
        for item in items2:
            dict[item[0]] = dict.get(item[0], 0) + item[1]
        for key, value in dict.items():
            answer.append([key, value])
        answer = sorted(answer)
        return answer