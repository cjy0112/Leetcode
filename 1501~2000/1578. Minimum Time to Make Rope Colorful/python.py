class Solution(object):
    def minCost(self, colors, neededTime):
        n=len(colors)
        l=0
        removes=0
        for r in range(n):
            if (colors[r]!=colors[l]):
                sameColors=neededTime[l:r]
                removes+=sum(sameColors)-max(sameColors)
                l=r
        removes+=sum(neededTime[l:])-max(neededTime[l:])
        return removes

# Using dynamic programming can solve.
# Here I use pointer concept to solve
