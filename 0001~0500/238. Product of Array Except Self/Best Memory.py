# we store multiplication of all numbers but 0 as mult_an 
# we store the count of all the 0 zero_count
# we go over each element in nums
# if element is 0:
#   if zero_count == 1:
#       save mult_an in that spot
#   else:
#       save 0 in that spot
# else:
#   if zero_count == 0:
#       save mult_an/element in that spot
#   else:
#       save 0 in that sopo

def get_0_count_and_mult(nums):
    mult = 1
    zero_count = 0
    for e in nums:
        if e==0:
            zero_count += 1
        else:
            mult *= e
            
    return mult, zero_count


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mult, zero_count = get_0_count_and_mult(nums)
        for i,e in enumerate(nums):
            if e == 0:
                if zero_count == 1:
                    nums[i] = mult
                else:
                    nums[i] = 0
            else:
                if zero_count == 0:
                    nums[i] = mult//e
                else:
                    nums[i] = 0
                    
        return nums
                    
                    
            
        
  
