class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a=dict()
        b=dict()
        for i in s:
            if i in a:
                a[i]+= 1
            else:
                a[i]= 1
        for j in t:
            if j in b:
                b[j]+= 1
            else:
                b[j]= 1
        if a==b:
            return 1
        else:
            return 0

        
