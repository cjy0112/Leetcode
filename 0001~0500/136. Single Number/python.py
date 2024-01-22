class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=[]
        for i in nums:
            if i not in temp:
                temp.append(i)
            else:
                temp.remove(i)
        return temp[0]
        

#runtime:711 ms win 28%
#memory:15.43mb win 71%
