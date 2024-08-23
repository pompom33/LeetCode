class Solution:
    def addDigits(self, num: int) -> int:
        digit = num
        while digit > 9:
            string = str(digit)
            digit = sum([int(c) for c in string])     
        return digit