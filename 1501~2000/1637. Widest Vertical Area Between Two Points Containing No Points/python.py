class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        a=set()
        for i in points:
            b=i[0]
            a.add(b)
        b=list(a)
        b=sorted(b)
        check=0
        for i in range(1,len(b)):
            temp=b[i]-b[i-1]
            check=max(check,temp)
        return(check)
        
