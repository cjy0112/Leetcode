class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return -1
        
        sorted_nums = sorted(nums)  # Correct sorting
        st = sorted_nums[0]  # Minimum value
        ed = sorted_nums[-1]  # Maximum value

        for i in sorted_nums:
            if i != st and i != ed:
                return i

        return -1  # Return -1 if no such element is found

        
        
