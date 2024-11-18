class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char == ".":
                    continue
                else:
                    row = board[i]

                    if row.count(char) > 1:
                        return False

                    count = 0
                    for k in range(9):
                        if board[k][j] == char:
                            count += 1

                    if count > 1:
                        return False

                    if self.check_sub(i,j,char,board) == False:
                        print(i,j,char)
                        return  False
        return True


    def check_sub(self,i,j,char,board):
        r = None
        if i < 3:
            r = range(0,3)
        elif i < 6:
            r = range(3,6)
        else:
            r = range(6,9)
        x = None
        y = None
        if j < 3:
            x = 0
            y = 3
        elif j < 6:
            x = 3
            y = 6
        elif j < 9:
            x = 6
            y = 9
        arr = []
        for k in r:
            arr += board[k][x:y]
            print(board[k][x:y])
        print(i,j)


        total = arr.count(char)
        return not (total > 1)
