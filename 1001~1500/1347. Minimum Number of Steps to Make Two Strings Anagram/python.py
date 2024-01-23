class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        return sum((Counter(t)-Counter(s)).values())
                

  # Runtime Win:27.006%
  # Memory  Win:99.96%
  # Using Python Counter function to solved
