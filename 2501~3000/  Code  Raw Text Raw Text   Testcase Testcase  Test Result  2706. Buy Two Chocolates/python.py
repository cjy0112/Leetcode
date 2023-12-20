class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        #print(prices)
        for i in range(0,len(prices)):
            rmd=money-int(prices[i])
            if(rmd-int(prices[i+1]))>=0:
                return (rmd-prices[i+1])
            else:
                return money
