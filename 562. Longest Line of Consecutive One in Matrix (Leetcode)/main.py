class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        lengths = []
        height = len(mat)
        width = len(mat[0])
        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    continue
                else:
                    diagonal_up = 0
                    i1 = i - 1
                    j1 = j - 1
                    while i1 >= 0 and j1 >= 0:
                        if mat[i1][j1] == 1:
                            diagonal_up += 1
                        else:
                            break
                        i1 -= 1
                        j1 -= 1

                    diagonal_down = 0
                    i1 = i + 1
                    j1 = j + 1
                    while i1 <= width and j1 <= height:
                        try:
                            if mat[i1][j1] == 1:
                                diagonal_down += 1
                            else:
                                break
                            i1 += 1
                            j1 += 1
                        except IndexError:
                            break

                    diagonal = 1 + diagonal_up + diagonal_down
                    lengths.append(diagonal)

                    left_length = 0
                    for k in range(j - 1, -1, -1):
                        try:
                            if mat[i][k] == 1:
                                left_length += 1
                            else:
                                break
                        except IndexError:
                            break

                    right_length = 0
                    for k in range(j + 1, len(mat[0])):
                        try:
                            if mat[i][k] == 1:
                                right_length += 1
                            else:
                                break
                        except IndexError:
                            break

                    horizontal_length = 1 + left_length + right_length
                    lengths.append(horizontal_length)

                    up_length = 0
                    for k in range(i - 1, -1, -1):
                        try:
                            if mat[k][j] == 1:
                                up_length += 1
                            else:
                                break
                        except IndexError:
                            break

                    down_length = 0
                    for k in range(i + 1, height):
                        try:
                            if mat[k][j] == 1:
                                down_length += 1
                            else:
                                break
                        except IndexError:
                            break
                    vertical = 1 + up_length + down_length
                    lengths.append(vertical)

                    anti_diagonal_up = 0
                    i1 = i - 1
                    j1 = j + 1
                    while i1 >= 0 and j1 < width:
                        try:
                            if mat[i1][j1] == 1:
                                anti_diagonal_up += 1
                            else:
                                break
                            i1 -= 1
                            j1 += 1
                        except IndexError:
                            break

                    anti_diagonal_down = 0
                    i1 = i + 1
                    j1 = j - 1
                    while i1 < height and j1 >= 0:
                        try:
                            if mat[i1][j1] == 1:
                                anti_diagonal_down += 1
                            else:
                                break
                            i1 += 1
                            j1 -= 1
                        except IndexError:
                            break
                    anti_diagonal = 1 + anti_diagonal_down + anti_diagonal_up
                    lengths.append(anti_diagonal)

        if lengths:
            return max(lengths)
        else:
            return 0






