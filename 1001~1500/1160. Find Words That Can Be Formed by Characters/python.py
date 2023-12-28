class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        result_length=0
        for i in words:
            # Check if the word can be formed by characters from chars
            if all(i.count(char) <= chars.count(char) for char in set(i)):
                result_length += len(i)

        return result_length
        
