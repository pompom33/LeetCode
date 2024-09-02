class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        answer = False
        char = ['a', 'c', 'e', 'g']
        string_1 = list(coordinate1)
        string_2 = list(coordinate2)
        if int(string_1[1]) % 2 == int(string_2[1]) % 2:
            if string_1[0] in char and string_2[0] in char:
                answer = True
            if string_1[0] not in char and string_2[0] not in char:
                answer = True 
        else:
            if string_1[0] in char and string_2[0] not in char:
                answer = True
            if string_1[0] not in char and string_2[0] in char:
                answer = True
        return answer