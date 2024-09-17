class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxes = 0
        prev_upper = 0
        for upper, percent in brackets:
            interval = upper - prev_upper
            if income < upper:
                interval = income - prev_upper
                taxes += interval * percent/100
                break       
            taxes += interval * percent/100  
            prev_upper = upper
        return taxes
