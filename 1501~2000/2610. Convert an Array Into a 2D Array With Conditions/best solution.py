class Solution(object):
    def findMatrix(self, nums):
        count = [0] * (max(nums)+1)
        for i in nums:
            count[i] += 1
        
        array=[]
        for i in range(max(count)):
            array.append([])
        for k in range(max(count)):
            for i in range(1,len(count)):
                if count[i] > 0:
                    array[k].append(i)
                    count[i]-=1
        return array
