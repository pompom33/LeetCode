class Solution:
    def freqAlphabets(self, s: str) -> str:
        nums = []
        answer = ""
        i = 0
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                nums.append(s[i:i+2])
                i += 3          
            else:
                nums.append(s[i])
                i += 1
        for num in nums:
            answer += chr(int(num) + 96)
        return answer