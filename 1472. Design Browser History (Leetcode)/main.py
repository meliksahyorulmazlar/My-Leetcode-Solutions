class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        if self.current != len(self.history) - 1:
            self.history = self.history[0:self.current + 1]
        self.history.append(url)
        self.current = len(self.history) - 1

    def back(self, steps: int) -> str:
        if self.current - steps < 0:
            self.current = 0
        else:
            self.current -= steps
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        if self.current + steps >= len(self.history) - 1:
            self.current = len(self.history) - 1
        else:
            self.current += steps

        return self.history[self.current]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)