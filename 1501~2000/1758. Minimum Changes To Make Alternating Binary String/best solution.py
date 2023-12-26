class Solution(object):
    def minOperations(self, s):
        a,b = '0','1'

        zr = 0
        for x in s:
            if(a != x):
                zr += 1
            a,b = b,a
        
        a,b = '1','0'
        on = 0
        for x in s:
            if(a != x):
                on += 1
            a,b = b,a
        return min(on,zr)
