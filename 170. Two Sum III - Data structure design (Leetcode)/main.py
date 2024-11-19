class TwoSum:

    def __init__(self):
        self.dictionary = {}
        return None

    def add(self, number: int) -> None:
        if number not in self.dictionary:
            self.dictionary[number] = 1
        else:
            self.dictionary[number] += 1

    def find(self, value: int) -> bool:
        for key, count in self.dictionary.items():
            n1 = key
            n2 = value - key
            if n2 == n1:
                if count >= 2:
                    print(n1, n2, count, value)
                    return True
            else:
                if n2 in self.dictionary:
                    return True

        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)