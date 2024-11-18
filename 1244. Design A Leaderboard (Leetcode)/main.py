class Leaderboard:

    def __init__(self):
        self.dictionary = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.dictionary:
            self.dictionary[playerId] = score
        else:
            self.dictionary[playerId] += score

    def top(self, K: int) -> int:
        results = self.dictionary.values()

        t = sorted(results)[len(results) - K:]

        return sum(t)

    def reset(self, playerId: int) -> None:
        self.dictionary[playerId] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)