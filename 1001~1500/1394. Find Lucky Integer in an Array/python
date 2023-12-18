class Solution(object):
    def findLucky(self, arr):
        temp=0
        if len(arr)==1 and arr[0]!=1:
            return -1
        else:
            for key, value in Counter(arr).items():
                print(key,value)
                if key==value:
                    temp=key
            if temp==0:
                return -1
            else:    
                return temp

