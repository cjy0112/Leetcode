class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c=Counter(arr)
        temp=[]
        for key, value in c.items():
            if value not in temp:
                temp.append(value)
            else:
                return False
        return True

# Runtime Win:41.93%
# Memory Win:41.13%
