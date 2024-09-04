class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        answer = False
        new_str_1 = s1[2] + s1[1] + s1[0] + s1[3]
        new_str_2 = s1[2] + s1[3] + s1[0] + s1[1]
        new_str_3 = s1[0] + s1[3] + s1[2] + s1[1]
        if s2 in [s1, new_str_1, new_str_2, new_str_3]:
            return True
        return answer