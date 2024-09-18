class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]

        for i in range(len(gain)):
            height = gain[i]
            length = len(altitudes)

            previous_height = altitudes[length - 1]

            new_altitude = height + previous_height

            altitudes.append(new_altitude)

        return max(altitudes)



