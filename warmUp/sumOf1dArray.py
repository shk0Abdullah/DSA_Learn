class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = [None] * len(nums)
        for i,k in enumerate(nums):
            arr[i] = sum(nums[:i+1])
        return arr
