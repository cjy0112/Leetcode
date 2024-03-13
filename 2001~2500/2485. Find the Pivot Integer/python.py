class Solution(object):
    def pivotInteger(self, n):
        check = 0
        for i in range(1, n + 1):
            check += i
            if sum(range(1, n + 1)) - check + i == check:
                return i
        return -1

# Runtime  Win:18.95%
# Memory   Win:15.69%

