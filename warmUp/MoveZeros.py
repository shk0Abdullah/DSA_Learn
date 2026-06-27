class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        x = (filter(lambda x: x!=0,nums)) 
        nums[:] = list(x)
        for i in range(zeros):
            nums.append(0)
        print(nums)