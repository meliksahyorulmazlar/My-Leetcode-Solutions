class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        new_time = arrivalTime + delayedTime
        while new_time >= 24:
            new_time -= 24
        return new_time
