class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = ["a","e","i","o","u"]
        count = 0
        words = words[left:right+1]
        for i in range(len(words)):
            word = words[i]
            if len(word) == 1 and word in vowels:
                count += 1
            else:
                if word[0] in vowels and word[-1] in vowels:
                    count += 1
        return count
