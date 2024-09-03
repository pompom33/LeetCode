class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        answer = ""
        string1 = str(num1).zfill(4)
        string2 = str(num2).zfill(4)
        string3 = str(num3).zfill(4)
        for key_tuple in zip(string1, string2, string3):
            answer += min(key_tuple)
        return int(answer)