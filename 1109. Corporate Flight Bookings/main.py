class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        #Prefix sum
        result = [0] * n

        for i, j, k in bookings:
            result[i - 1] += k
            if j == n:
                continue
            else:
                result[j] -= k

        for i in range(1, n):
            result[i] = result[i - 1] + result[i]

        return result
