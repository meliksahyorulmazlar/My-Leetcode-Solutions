class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        if k == 0:
            return [0] * len(code)
        else:
            length = len(code)
            result = []
            if k>0:
                for i in range(length):
                    count = 0
                    for j in range(1,k+1):
                        new_index = i + j
                        if new_index >= length:
                            new_index -= length
                        count += code[new_index]
                    result.append(count)
            else:
                for i in range(length):
                    count = 0
                    for j in range(1,-k+1):
                        new_index = i - j
                        print(new_index)
                        count += code[new_index]
                        print(new_index)
                    result.append(count)

            return result

sol = Solution()
sol.decrypt([2,4,9,3],k=-2)
