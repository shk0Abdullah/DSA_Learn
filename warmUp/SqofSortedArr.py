
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        print(abs(nums[0]))
        for i,k in enumerate(nums):
            nums[i] = (abs(nums[i])**2)
        return sorted(nums)
            