class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        nums = range(1,n+1)
        num1, num2 = 0,0
        for number in nums:
            if number % m == 0:
                num1 += number
            else:
                num2 += number
        
        return num2-num1
