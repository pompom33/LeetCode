class Solution:
    def makeFancyString(self, s: str) -> str:
        listed = list(s)
        answer = listed[:2]
        for i in range(2, len(listed)):
            prev_2 = listed[i-2]
            prev_1 = listed[i-1]
            present = listed[i]
            if prev_2 == prev_1 and prev_1 == present:
                continue
            answer.append(present)
        return "".join(answer)