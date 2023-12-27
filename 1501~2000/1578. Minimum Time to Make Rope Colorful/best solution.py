class Solution(object):
    def minCost(self, colors, time):
        n = len(colors)
        ans = 0
        for i in xrange(n-1):
            if colors[i] == colors[i+1]:
                if time[i] > time[i+1]:
                    ans += time[i+1]
                    time[i+1] = time[i]
                else:
                    ans += time[i]
        return ans

#Best solution
