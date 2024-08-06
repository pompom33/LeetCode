class Solution:
    def countPoints(self, rings: str) -> int:
        answer = 0
        rod_dict = defaultdict(set)
        for i in range(0, len(rings), 2):
            rod_dict[rings[i+1]].add(rings[i])
        for rod in rod_dict.values():
            if len(rod) == 3:
                answer += 1
        return answer