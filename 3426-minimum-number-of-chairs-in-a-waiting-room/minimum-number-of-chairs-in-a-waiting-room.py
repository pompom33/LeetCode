class Solution:
    def minimumChairs(self, s: str) -> int:
        cnt = 0
        answer = []
        for c in s:
            if c == 'E':
                cnt += 1
            else:
                cnt -= 1
            answer.append(cnt)
        return max(answer)