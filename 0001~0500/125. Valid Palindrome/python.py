class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c for c in lower(s) if c.isalnum())
        if s ==s[::-1]:
            return True
        else:
            return False
        
# Runtime   Win:72.75%
# Memory    Win:71.40%
