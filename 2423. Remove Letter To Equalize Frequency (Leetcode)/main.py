class Solution:
    def equalFrequency(self, word: str) -> bool:
        dictionary = {}
        for char in word:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1

        values = [n for n in dictionary.values()]

        greatest = max(values)
        smallest = min(values)

        list1 = []
        greatest_found = True
        for n in values:
            if n == greatest:
                if greatest_found:
                    greatest_found = False
                    new_num = n - 1
                    if new_num == 0:
                        continue
                    else:
                        list1.append(new_num)
                else:
                    list1.append(n)
            else:
                list1.append(n)

        list2 = []
        smallest_found = True
        for n in values:
            if n == smallest:
                if smallest_found:
                    smallest_found = False
                    new_num = n - 1
                    if new_num == 0:
                        continue
                    else:
                        list2.append(new_num)
                else:
                    list2.append(n)
            else:
                list2.append(n)

        if len(set(list1)) == 1 or len(set(list2)) == 1:
            return True
        return False

sol = Solution()
sol.equalFrequency("cbccca")