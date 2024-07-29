class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        answer = True
        for i in range(len(s)):
            if s[i] in s_dict:
                if s_dict[s[i]] != t[i]:
                    answer = False
            else:
                if t[i] in s_dict.values():
                    answer =  False
                s_dict[s[i]] = t[i]
        return answer