class Solution:
    def reformatNumber(self, number: str) -> str:
        tmp = ""
        answer = ""
        for c in number:
            if c.isdigit():
                tmp += c     
        for i in range(0, len(tmp), 3):
            if len(tmp) % 3 == 1:
                if i == len(tmp)-4:
                    answer = answer + tmp[i:i+2] + "-"
                    answer = answer + tmp[i+2:]
                    break
            if i >= len(tmp)-3:
                answer = answer + tmp[i:i+3]
                break
            answer = answer + tmp[i:i+3] + "-"
        return answer
