class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0]*(len(gain)+1)
        for i,_ in enumerate(gain):
            arr[i] = sum(gain[:i+1])
        print(arr)
        return max(arr)