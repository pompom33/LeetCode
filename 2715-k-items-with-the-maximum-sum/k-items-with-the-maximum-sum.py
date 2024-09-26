class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes + numZeros:
            if k < numOnes:
                answer = k
            else:
                answer = numOnes
        else:
            answer = numOnes - (k-numOnes-numZeros)
        return answer