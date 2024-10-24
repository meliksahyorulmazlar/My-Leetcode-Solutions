class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        f = {}
        for num in nums:
            if num not in f:
                f[num] = 1
            else:
                f[num] += 1

        result = sorted(f, key=lambda x: (f[x], -x))

        output = []

        for number in result:
            amount = f[number]
            if amount > 1:
                for i in range(amount):
                    output.append(number)
            else:
                output.append(number)

        return output
