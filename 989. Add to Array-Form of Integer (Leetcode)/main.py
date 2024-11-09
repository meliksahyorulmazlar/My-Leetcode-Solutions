import sys

sys.set_int_max_str_digits(100000)


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        new_num = int("".join([str(n) for n in num]))
        new_num += k
        return [int(n) for n in list(str(new_num))]