class Solution(object):
    def findPeaks(self, mountain):
        peaks = []
        for i in range(1,len(mountain)-1):
            previous_item = mountain[i-1]
            current_item = mountain[i]
            next_item = mountain[i+1]
            if current_item > previous_item and current_item > next_item:
                peaks.append(i)
        return peaks
