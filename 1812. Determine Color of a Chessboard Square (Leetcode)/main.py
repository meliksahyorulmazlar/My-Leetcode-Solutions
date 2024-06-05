class Solution(object):
    def squareIsWhite(self, coordinates):
        mapping = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
        first = mapping[coordinates[0]]
        second = int(coordinates[1])
        if (first % 2) == (second%2):
            return False
        else:
            return True