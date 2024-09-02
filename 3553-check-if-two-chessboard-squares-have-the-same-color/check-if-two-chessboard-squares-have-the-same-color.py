class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        answer = False
        loc_1 = ord(coordinate1[0]) + int(coordinate1[1])
        loc_2 = ord(coordinate2[0]) + int(coordinate2[1])
        if loc_1 % 2 == loc_2 % 2:
            answer = True
        return answer