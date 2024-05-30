class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hours_angle = (hour+(minutes/60))*30
        if hours_angle >= 360:
            hours_angle -= 360
        minutes_angle = (minutes/60)*360
        if abs(hours_angle-minutes_angle) > 180:
            return 360 -abs(hours_angle-minutes_angle)
        else:
            return abs(hours_angle-minutes_angle)