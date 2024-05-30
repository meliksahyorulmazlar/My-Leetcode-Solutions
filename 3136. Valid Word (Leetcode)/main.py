class Solution:
    def isValid(self, word: str) -> bool:
        vowels =  ["a","e","i","o","u"]
        letters = ['b', 'c', 'd','f', 'g', 'h','j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        is_vowel = False
        is_consonant= False
        word = word.lower()
        if len(word) >= 3:
            for char in word:
                if char in vowels:
                    is_vowel = True
                if char in letters:
                    is_consonant= True
                if char not in vowels and char not in letters and char not in numbers:
                    return False
        else:
            return False
        if is_vowel == True and is_consonant== True:
            return True
        else:
            return False
