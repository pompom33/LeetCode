class Solution:
    def sumZero(self, n: int) -> List[int]:
         return [i for i in range(-n+1, n, 2)]