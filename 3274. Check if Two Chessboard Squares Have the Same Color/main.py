class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        original_black = ["a", "c", "e", "g"]
        original_white = ["b", "d", "f", "h"]

        if coordinate1[0] in original_black:
            if int(coordinate1[1]) % 2 == 0:
                c1 = "white"
            else:
                c1 = "black"
        elif coordinate1[0] in original_white:
            if int(coordinate1[1]) % 2 == 0:
                c1 = "black"
            else:
                c1 = "white"

        if coordinate2[0] in original_black:
            if int(coordinate2[1]) % 2 == 0:
                c2 = "white"
            else:
                c2 = "black"
        elif coordinate2[0] in original_white:
            if int(coordinate2[1]) % 2 == 0:
                c2 = "black"
            else:
                c2 = "white"

        if c1 == c2:
            return True
        else:
            return False
