class Solution(object):
    def makeEqual(self, words):
        # Count the frequency of each character in all the strings
        char_count = {}
        for word in words:
            for char in word:
                if char not in char_count:
                    char_count[char] = 0
                char_count[char] += 1

        # Check if the frequency of each character is divisible by the number of strings
        for char, count in char_count.items():
            if count % len(words) != 0:
                return False

        return True
