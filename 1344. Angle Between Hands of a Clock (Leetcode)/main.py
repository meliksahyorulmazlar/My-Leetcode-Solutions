class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_angle = minutes * 6
        hour_angle = (hour+(minutes/60))*30
        
        if hour_angle >= 360:
            hour_angle -= 360

        angle1 = abs(minutes_angle-hour_angle)
        angle2 = 360-option1

        #Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand. 
        #The leetcode question is asking for the smaller angle
        return min(angle1,angle2)
