class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        array = [i for i in range(1, n + 1)]
        index = 0
        forward = True

        for i in range(time):
            if forward:
                index += 1
            else:
                index -= 1
            item = array[index]

            if item == n:
                forward = False

            if item == 1:
                forward = True
        return index + 1



