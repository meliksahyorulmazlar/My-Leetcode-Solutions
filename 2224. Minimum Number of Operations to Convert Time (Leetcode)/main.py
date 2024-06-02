class Solution(object):
    def convertTime(self, current, correct):
        t1 = current.split(":")
        t2 = correct.split(":")
        t1 = (int(t1[0])*60) + int(t1[1])
        t2 = (int(t2[0])*60) + int(t2[1])
        time = t2-t1
        count = 0
        while time >0:
            if time >=60:
                time-=60
                count +=1
            elif time >=15:
                time-=15
                count +=1
            elif time >=5:
                time-=5
                count +=1
            elif time >=1:
                time-=1
                count += 1
        return count

s = Solution()
s.convertTime("02:30","04:35")

