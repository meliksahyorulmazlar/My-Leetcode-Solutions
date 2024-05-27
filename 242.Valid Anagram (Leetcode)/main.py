class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s not in s_dict:
                s_dict[char_s] = 1
            else:
                s_dict[char_s] += 1

            if char_t not in t_dict:
                t_dict[char_t] = 1
            else:
                t_dict[char_t] += 1
        if s_dict == t_dict:
            return True
        else:
            return False