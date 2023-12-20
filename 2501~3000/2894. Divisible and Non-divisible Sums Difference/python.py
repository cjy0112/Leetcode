class Solution(object):
    def differenceOfSums(self, n, m):
        a=sum(range(n+1))
        temp=0
        for i in range(1,n+1):
            if i%m==0:
                temp+=i
        return int((a-temp)-temp)
        
