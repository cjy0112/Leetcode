class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        number=0
        for i in range(0,len(startTime)):
            if startTime[i]<=queryTime<=endTime[i]:
                number+=1
        return number
