class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        i = 0
        while i < n:
            if i + 2 < n and nums[i + 2] - nums[i] <= k:
                res.append([nums[i], nums[i + 1], nums[i + 2]])
                i += 3
            else:
                return []
        return res
