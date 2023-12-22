class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        for i in range(0,len(s)):
            if i==0:
                a=s[i].count('0')
                b=s[i+1:len(s)].count('1')
                c=max(c,a+b)
            else:
                a=s[:i].count('0')
                b=s[i:len(s)].count('1')
                c=max(c,a+b)
        return c
