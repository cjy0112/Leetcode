class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        GOAL: find the max amount of money you can rob without alerting police 
        input: 
        * INT arr -- nums 
        output: 
        * INT val of max amount of money to rob 

        RULES 
        1) nums[i] = how much money you can get from robbing ith house 
        2) robbing 2 adjacent houses will alert the cops

        NOTES: 
        runthrough 
        [1,2,3,1]
        1 or not -- 1 
        1 or 2 -- 2 
        3 + 1 or rob 2 -- 4 
        1 + 2 or rob 4 -- 3 

        optimalchoice(rob i + i-2, take dp[i-1])
        base cases: rob house 0 -- dp[0], rob house 1 -- dp [1]
        """
        if not nums: 
            return 0
        if len(nums) == 1: 
            return nums[0]
        if len(nums) == 2: 
            return max(nums)
        dp = [-1] * len(nums) 
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)): 
            dp[i] = max(dp[i - 2] + nums[i], dp[i-1])

        print(dp)
        return dp[len(nums) - 1]
    

        

      # Best Runtime
