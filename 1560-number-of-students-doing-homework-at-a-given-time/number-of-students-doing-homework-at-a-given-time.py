class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        answer = 0
        for time in zip(startTime, endTime):
            if time[0] <= queryTime and time[1] >= queryTime:
                answer += 1
        return answer
            