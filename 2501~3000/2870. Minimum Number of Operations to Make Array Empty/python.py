class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c1=Counter(nums)
        count=0
        print(c1)
        for key in c1.values():
            a=key//3
            b=key%3
            print(a,b)
            if b==0:
                count=count+a
            else:
                if a==0 and b==1:
                    return -1
                if a==0 and b==2:
                    count=count+1
                else:
                    count=count+a+1
        return count
            
            
        
  # Runtime:621ms win:31.58%
  # Memory: 31.74mb win:10.53%
