class Solution(object):
    def halvesAreAlike(self, s):
        half_length = len(s) // 2
        first_half = s[:half_length]
        second_half = s[half_length:]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        first_count = 0
        second_count = 0
        for i in first_half:
            if i in vowels:
                first_count += 1
        for j in second_half:
            if j in vowels:
                second_count += 1
        
        return first_count == second_count
