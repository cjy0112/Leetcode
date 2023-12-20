class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        a=prices[0]+prices[1]
        if a==money:
            return 0
        elif money-a<0:
            return money
        else:
            return money-a

