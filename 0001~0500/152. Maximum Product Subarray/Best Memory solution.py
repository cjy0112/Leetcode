class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        product = 1
        res = nums[0]

        for num in nums:
            product = product * num
            res = max(res, product)
            if num == 0:
                product = 1
            
        product = 1
        for num in reversed(nums):
            product = product * num
            res = max(res, product)
            if num == 0:
                product = 1
        
        return res

# Using Kadane's Algorithm to solve
