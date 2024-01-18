class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        before1=1
        before2=2
        x=0
        for i in range(2,n):
            x=before1+before2
            before1=before2
            before2=x
        return x
            

# Runtime Win:62.78%
# Memory  Win:98.31%
# The concept used Dynamic programmaring to solve
