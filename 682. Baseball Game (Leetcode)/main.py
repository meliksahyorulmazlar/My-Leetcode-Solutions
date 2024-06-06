class Solution(object):
    def calPoints(self, operations):
        numbers = "0123456789"
        record = []

        for op in operations:
            if op == "+":
                one = int(record[-1])
                two = int(record[-2])
                record.append(one+two)
            elif op == "D":
                one = int(record[-1])
                record.append(one*2)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        return sum(record)
