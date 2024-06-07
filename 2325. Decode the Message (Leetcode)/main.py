class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dictionary = {}
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']

        encrypted = list(key.replace(" ",""))
        current_index = 0
        for char in encrypted:
            if char not in dictionary:
                dictionary[char] = letters[current_index]
                current_index += 1
            else:
                continue
        new_string = ""
        for char in message:
            if char in dictionary:
                new_string += dictionary[char]
            else:
                new_string += char
        return new_string










sol = Solution()
sol.decodeMessage(key="the quick brown fox jumps over the lazy dog",message="vkbs bs t suepuv")