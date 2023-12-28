class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        c_1 = ''.join(word1)
        c_2 = ''.join(word2)
        if c_1 !=c_2:
            return False
        else:
            return True

        

