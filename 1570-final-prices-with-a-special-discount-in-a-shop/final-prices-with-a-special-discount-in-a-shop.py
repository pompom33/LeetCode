class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i+1,len(prices)):
                if prices[i] >= prices[j]:
                    discount = prices[j]
                    answer.append(prices[i] - discount)
                    break
            if not discount:
                answer.append(prices[i])
        return answer
