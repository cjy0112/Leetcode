class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        dict = {}

        for i in arr:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        uniques = len(dict)
        counter = 1

        while k > 0:
            count = list(dict.values()).count(counter)
            mult = count * counter
            if  mult < k:
                uniques -= count
                k -= mult
            else:
                uniques -= k//counter
                break
            counter += 1 
        
        return uniques



