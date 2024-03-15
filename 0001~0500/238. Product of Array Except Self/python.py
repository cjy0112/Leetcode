class Solution(object):
    def productExceptSelf(self, nums):
        number=nums.count(0)
        if number==0:
            total=1
            temp=[]
            for i in nums:
                total=total*i
            for i in nums:
                temp.append(total/i)
            return temp
        elif number >=2:
            temp=[0]*len(nums)
            return temp
        else:
            total=1
            temp = [0] * len(nums)
            check=[]
            for i in range(0,len(nums)):
                if nums[i]==0:
                    check.append(i)
                else:
                    total=total*nums[i]
            temp[check[0]]=total
            return temp
            
        
# Runtime  Win:98.39%
# Memory   Win:95.07%
