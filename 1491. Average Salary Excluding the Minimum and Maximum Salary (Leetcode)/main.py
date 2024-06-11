class Solution:
    def average(self, salary: List[int]) -> float:
        length = len(salary) - 2
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary)/length