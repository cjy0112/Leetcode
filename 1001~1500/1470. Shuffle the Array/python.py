class Solution(object):
    def shuffle(self, nums, n):
        temp=[]
        for i in range(0,n):
            temp.append(nums[i])
            temp.append(nums[i+n])
        return(temp)
