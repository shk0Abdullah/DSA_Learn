class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        inc = 0
        for each in stones:
            if each in jewels:
                inc = inc +1
        return inc