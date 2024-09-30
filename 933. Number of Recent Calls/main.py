class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        lower_bound = t - 3000
        upper_bound = t
        result = 0
        for r in self.requests:
            if lower_bound <= r <= upper_bound:
                result += 1

        return result

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)