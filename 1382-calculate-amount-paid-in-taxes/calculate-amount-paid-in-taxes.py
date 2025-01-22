class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        prev_upper= 0
        answer = 0
        for upper, percent in brackets:
            percentage = percent/100
            target_income = min(upper, income)
            answer += (target_income-prev_upper)*percentage

            prev_upper = upper
            
            if upper >= income:
                break
        return answer