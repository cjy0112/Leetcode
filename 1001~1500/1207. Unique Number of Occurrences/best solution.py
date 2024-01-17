class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        found = set()
        i = 0
        while i < len(arr):
            count = 1
            cur = arr[i]
            i+=1
            while i < len(arr) and arr[i] == cur :
                count +=1
                i+=1
            if count in found:
                return False
            found.add(count)
        return True
