class Solution(object):
    def heightChecker(self, heights):
        count = 0
        all_expected = sorted(heights)
        for i in range(len(heights)):
            height = heights[i]
            expected = all_expected[i]
            if height != expected:
                count += 1
        return count
