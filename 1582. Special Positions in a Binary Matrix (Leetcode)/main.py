class Solution(object):
    def numSpecial(self, mat):
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    if mat[i].count(1) == 1:
                        lc = 0
                        for m in mat:
                            if m[j] == 0:
                                lc +=1
                        if lc == len(mat)-1:
                            count +=1
        return count

