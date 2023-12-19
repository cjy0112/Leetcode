class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ptr_a = 0
        ptr_b = n

        ret = []

        while ptr_b < len(nums):
            ret.append(nums[ptr_a])
            ret.append(nums[ptr_b])

            ptr_a += 1
            ptr_b += 1

        return ret
