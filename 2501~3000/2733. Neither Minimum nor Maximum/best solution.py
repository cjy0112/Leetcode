class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return -1

        nums.sort()
        if nums[0] == nums[-1]:
            return -1
        
        for num in nums:
            if num != nums[0] and num != nums[-1]:
                return num
        return -1
