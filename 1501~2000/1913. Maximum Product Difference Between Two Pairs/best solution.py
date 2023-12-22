class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        big1 = 0
        big2 = 0
        small1 = 10 ** 4
        small2 = 10 ** 4
        for i in nums:
            if i > big1:
                big2 = big1
                big1 = i
                
            elif i > big2:
                big2 = i
                
            if i < small1:
                small2 = small1
                small1 = i
                
            elif i < small2:
                small2 = i
                
        # print([small1,small2,big1,big2])
        return big1 * big2 - small1 * small2
