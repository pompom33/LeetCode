class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        sorted_seats = sorted(seats)
        sorted_students = sorted(students)
        answer = 0
        for seat, student in zip(sorted_seats, sorted_students):
            answer += abs(seat - student)
        return answer
