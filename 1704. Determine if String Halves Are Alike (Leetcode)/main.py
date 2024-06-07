class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        else:
            s = s.lower()
            vowels = ["a","e","i","o","u"]
            half = len(s)//2
            s1 = s[0:half]
            s2 = s[half:]
            s1_count = 0
            s2_count = 0
            for item in s1:
                if item in vowels:
                    s1_count += 1
            for item in s2:
                if item in vowels:
                    s2_count += 1
            if s1_count == s2_count:
                return True
            else:
                return False

