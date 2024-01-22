class Solution(object):
    def findErrorNums(self, nums):
        dic=Counter(nums)
        n=len(nums)
        for i,j in dic.items():
            if j==2:
                rep=i
        miss=(n*(n+1))//2-(sum(nums)-rep)
        return [rep,miss]
                

# Runtime Win:36.62%
# Memory  Win:83.1%
