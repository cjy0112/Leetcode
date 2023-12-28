class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        amount = {}
        for char in chars:
            amount[char] = chars.count(char)
        sum_length = 0
        for word in words:
            for char in word:
                if word.count(char) > chars.count(char):
                    break
            else:
                sum_length += len(word)
        return sum_length
