class Solution(object):
    def minOperations(self, s):
        ptr = True
        op = {True: "1", False: "0"}
        cnta = cntb = 0
        for i in range(len(s)):
            if s[i] != op[ptr]:
                cnta += 1
            if s[i] != op[not ptr]:
                cntb += 1
            ptr = not ptr

        return min(cnta, cntb)

