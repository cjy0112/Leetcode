class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = sqrt(n * (n + 1) // 2)
        return -1 if x % 1 else int(x)


# Explan: https://www.youtube.com/watch?si=ZfzW277GDKkCbzCW&embeds_referring_euri=https%3A%2F%2Fleetcode.com%2F&source_ve_path=Mjg2NjQsMTY0NTA2&feature=emb_share&v=ET11YA6g4wQ



