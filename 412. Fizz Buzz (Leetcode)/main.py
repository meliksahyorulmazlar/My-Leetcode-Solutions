class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list = []
        for i in range(1,n+1):
            if i % 15 == 0:
                list.append("FizzBuzz")
                continue
            elif i % 5 == 0:
                list.append("Buzz")
                continue
            elif i % 3 == 0:
                list.append("Fizz")
                continue
            else:
                list.append(str(i))
        return list
    
