class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dic = defaultdict(int)
        lucky = -1

        for num in arr:
            dic[num] += 1

        for num in dic:
            if num == dic[num]:
                lucky = max(num, lucky)

        return lucky
