class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start < destination:
            clockwise = sum(distance[start : destination])
        else:
            clockwise = sum(distance[destination:start])
        counter_clockwise =  sum(distance) - clockwise
        return min(clockwise, counter_clockwise)
