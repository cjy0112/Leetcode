class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=sorted(nums)
        return ((a[len(nums)-1]*a[len(nums)-2])-(a[0]*a[1]))
