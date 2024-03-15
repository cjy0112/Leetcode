class Solution(object):
    def maxProduct(self, nums):
        cur,total,i=1,-10,0
        for i in range(0,len(nums)):
            cur=cur*nums[i]
            total=max(total,cur)
            if cur==0:
                cur=1
        cur=1
        for i in range(len(nums)-1,-1,-1):
            cur=cur*nums[i]
            total=max(total,cur)
            if cur==0:
                cur=1
        return total
                
# Runtime Win:32.98%
# Memory  Win:19.78%
