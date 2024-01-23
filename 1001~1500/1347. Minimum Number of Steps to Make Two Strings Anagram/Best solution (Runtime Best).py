class Solution(object):
    def minSteps(self, s, t):
        p=0
        for i in set(s):
            k=s.count(i)
            l=t.count(i)
            if k>l:
                p=p+(k-l)
        return p
        """
        :type s: str
        :type t: str
        :rtype: int
        """
