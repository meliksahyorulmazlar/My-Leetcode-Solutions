class FrequencyTracker:

    def __init__(self):
        self.dictionary = {}

    def add(self, number: int) -> None:
        if number not in self.dictionary:
            self.dictionary[number] = 1
        else:
            self.dictionary[number] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.dictionary:
            if self.dictionary[number] != 0:
                self.dictionary[number] -= 1

    def hasFrequency(self, frequency: int) -> bool:

        x = None
        for key, value in self.dictionary.items():
            if value == frequency:
                return True

        return False

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)