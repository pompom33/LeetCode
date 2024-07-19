class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        tmp = ""
        nums = []
        for c in word:
            if c.isnumeric():
                tmp += c
            elif tmp:
                nums.append(int(tmp))
                tmp = ""
        if tmp:
            nums.append(int(tmp))
        return len(set(nums))