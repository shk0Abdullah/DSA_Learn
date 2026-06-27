class Solution:
    def reverseVowels(self, s: str) -> str:
        pointer_start = 0
        pointer_end = -1
        vowels = "aeiouAEIOU"
        s= list(s)
        while pointer_start < len(s)+pointer_end:
            if s[pointer_start] not in vowels:
                pointer_start +=1
            elif s[pointer_end] not in vowels:
                pointer_end -=1
            else:
                s[pointer_start],s[pointer_end] = s[pointer_end] ,s[pointer_start]
                pointer_start +=1
                pointer_end -=1

        s =("".join(s))
        print(s)
        return s
            
            