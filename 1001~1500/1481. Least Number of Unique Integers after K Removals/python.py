class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        a=Counter(arr)
        sorted_counter = sorted(a.items(), key=lambda x: x[1])
        while k > 0:
            key, value = sorted_counter[0]
            value -= 1
            if value == 0:
                sorted_counter.pop(0)
            else:
                sorted_counter[0] = (key, value)
            k -= 1
        return len(sorted_counter)

# Runtime Win:5.11%
# Memory  Win:36.33%
