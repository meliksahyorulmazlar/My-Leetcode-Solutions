class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new_numbers = []
        for n in numbers:
            if n not in new_numbers:
                new_numbers.append(n)
            if new_numbers.count(n) == 1:
                new_numbers.append(n)

        for n in new_numbers:
            other_pair = target-n
            if other_pair in new_numbers:
                if other_pair == n:
                    first_index = numbers.index(n)
                    second_index = numbers.index(n,first_index+1)
                    return [first_index+1,second_index+1]
                else:
                    first_index = numbers.index(n)
                    second_index = numbers.index(other_pair)
                    return [first_index+1,second_index+1]
