class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', "")
        number = number.replace('-', "")
        answer = []
        while len(number) > 4:
            answer.append(number[:3])
            number = number[3:]
        if len(number) == 4:
            answer.append(number[:2])
            number = number[2:]
            answer.append(number[:2])
            number = number[2:]
        else:
            answer.append(number[:3])
        return "-".join(answer)