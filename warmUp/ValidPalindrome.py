class Solution:
    def isPalindrome(self, s: str) -> bool:
        extras = '''!@#$%^&*()_+-=}{][\|':;.",/?`~'''
        s = "".join(filter(lambda x: x not in extras,s))
        s = s.replace(" ","").strip().lower()
        print(s)
        pointer_start = 0 
        pointer_end = -1
        while pointer_start < len(s)+pointer_end:
            if s[pointer_start] == s[pointer_end]:
                pointer_start +=1
                pointer_end -=1 
                continue
            else:
                return False
        return True
  