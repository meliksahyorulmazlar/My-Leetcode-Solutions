class Solution(object):
    def minimumChairs(self, s):
        occupancy = []
        count = 0
        for char in s:
            if char == "E":
                count += 1
                occupancy.append(count)
            elif char == "L":
                count -=1
                occupancy.append(count)
        return max(occupancy)

