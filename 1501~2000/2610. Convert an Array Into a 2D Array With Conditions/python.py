class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = Counter(nums)
        freq=max(count.values())
        s=[[]for i in range(freq)]
        for nums, freq in count.items():
            for i in range(freq):
                s[i].append(nums)
        return s


        
# runtimes:33ms
# memory: 13.32mb 
# not well
