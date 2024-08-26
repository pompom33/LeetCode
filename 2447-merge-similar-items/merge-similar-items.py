class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dict = {}
        for item in items1 + items2:
            dict[item[0]] = dict.get(item[0], 0) + item[1]
        answer = [[key, value] for key, value in dict.items()]    
        return sorted(answer)