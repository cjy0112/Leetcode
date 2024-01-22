class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp={}
        for i in range(0,len(nums)):
            if i<2:
                temp[i]=nums[i]
            elif i==2:
                temp[i]=nums[i]+temp[i-2]
            else:
                temp[i]=nums[i]+max(temp[i-2],temp[i-3])       
        return max(temp.values())        

# Runtime Win:49.29%
# Memory  Win:99.70%

