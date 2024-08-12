class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for i in range(len(prices)):
            discounted = False
            for j in range(i+1,len(prices)):
                if prices[i] >= prices[j]:
                    answer.append(prices[i] - prices[j])
                    discounted = True
                    break
            if not discounted:
                answer.append(prices[i])
        return answer
