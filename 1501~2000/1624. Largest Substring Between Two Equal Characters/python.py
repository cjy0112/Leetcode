class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp={}
        length = -1
        for i in range(0,len(s)):
            for j in range(i+1,len(s)):
                if s[j]==s[i]:
                    length = max(length, int(j - i - 1))
        return length



            
        
