class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
        result = 0
        for key, value in cnt.items():
            if value < 2:
                return -1
            r3 = value%3
            if r3 == 0:
                result += (value//3)
            else:
                result += (value//3 + 1)
        return result
