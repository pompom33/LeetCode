class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        answer = True
        if num == 0:
            return True
        if str(num).startswith('0') or str(num)[::-1].startswith('0'):
            return False
        return answer