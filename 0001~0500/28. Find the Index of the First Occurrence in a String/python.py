class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        else:
            return haystack.find(needle)
        
# runtime:13 ms win:68%
# memory :13.23 mb win:83%
