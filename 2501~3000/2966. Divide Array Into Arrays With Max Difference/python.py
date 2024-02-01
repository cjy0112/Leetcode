class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        temp=sorted(nums)
        final=[[temp[0]]]
        compare=temp[0]
        for i in range(1,len(temp)):
            if len(final[-1])<3:
                if temp[i]-compare<=k:
                    final[-1].append(temp[i])
                    compare=min(final[-1])
                else:
                    return []
            else:
                final.append([temp[i]])
                compare=temp[i]
        return final
            
                
# Runtime Win:9.33%
# Memory  Win:48.22%  
