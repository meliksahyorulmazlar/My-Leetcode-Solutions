class ZigzagIterator:
    def __init__(self, v1: list[int], v2: list[int]):
        self.count = 0
        self.v1 = v1
        self.v2 = v2
        self.v1_count = 0
        self.v2_count = 0

    def next(self) -> int:
        if self.v1 and self.v2:
            if self.count % 2 == 0:
                self.count += 1
                return self.v1.pop(0)
            else:
                self.count += 1
                return self.v2.pop(0)

        elif self.v1:
            return self.v1.pop(0)
        else:
            return self.v2.pop(0)


    def hasNext(self) -> bool:
        if self.v1 or self.v2:
            return True
        return False

if __name__ == "__main__":
    v1 = [1, 2]
    v2 = [3, 4, 5, 6]
    i, v = ZigzagIterator(v1, v2), []
    while i.hasNext():
        v.append(i.next())
    print(v)