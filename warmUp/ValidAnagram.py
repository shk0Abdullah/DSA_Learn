class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for i in t:
                if i not in s:
                    return False
                else:
                    x = s.find(i)
                    s = s[:x]+s[x+1:]
            return True
        else:
            return False