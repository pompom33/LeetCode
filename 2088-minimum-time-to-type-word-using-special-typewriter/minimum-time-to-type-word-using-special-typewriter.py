class Solution:
    def minTimeToType(self, word: str) -> int:
        answer = 0
        cur_loc = 97
        for c in word:
            new_loc = ord(c)
            clockwise = abs(new_loc - cur_loc)
            counter_clockwise = 26 - abs(new_loc - cur_loc)
            print(cur_loc, min(clockwise, counter_clockwise), clockwise, counter_clockwise)
            answer += min(clockwise, counter_clockwise)
            cur_loc = new_loc
        return answer + len(word)