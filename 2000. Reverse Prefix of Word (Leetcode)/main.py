class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            reverse_string = ''
            index = 0
            for i in range(len(word)):
                char = word[i]
                if char == ch:
                    reverse_string += char
                    index = i+1
                    break
                else:
                    reverse_string += char
            return reverse_string[::-1] + word[index:]
