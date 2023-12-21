class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        x_axis = sorted({ x for x,y in points})

        maxDif = 0
        for i in range(1, len(x_axis)):
            maxDif = max(maxDif, x_axis[i] - x_axis[i-1])
        
        return maxDif
