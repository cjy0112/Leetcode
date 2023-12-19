class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        for i in nums:
            number= str(i)
            if len(number) %2==0:
                a+=1
        return a
