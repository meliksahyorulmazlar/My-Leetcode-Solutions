class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        greatest = max(candies)
        for candy in candies:
            if (candy + extraCandies) >= greatest:
                output.append(True)
            else:
                output.append(False)

        return output


