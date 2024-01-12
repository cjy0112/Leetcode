class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a ,b =0 ,0
        first, second = s[:len(s)/2], s[len(s)/2 :]
        for char in first:
            if char in check:
                a +=1
        for char in second:
            if char in check:
                b +=1
        if a ==b:
            return True
        else:
            return False

# Runtime Win:8.61 %
# Memory  Win:59.98 %
