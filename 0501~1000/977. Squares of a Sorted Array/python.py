class Solution(object):
    def sortedSquares(self, nums):
        for i in range(0,len(nums)):
            nums[i]=int(nums[i])*int(nums[i])
        return sorted(nums)
