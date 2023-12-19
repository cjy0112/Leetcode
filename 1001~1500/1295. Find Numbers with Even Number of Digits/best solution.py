class Solution(object):
    def findNumbers(self, nums):
        counter1 = 0;
        for i in nums:
            counter2 = 1;
            while(i) != 0:
                print("current i", i, "current counter2", counter2, "current counter1", counter1)
                i = i/10
                counter2 += 1
                counter2 = counter2%2
            counter1 += counter2
        return counter1
