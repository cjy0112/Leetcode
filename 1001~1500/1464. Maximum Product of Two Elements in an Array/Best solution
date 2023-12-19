class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # Inicializa los dos mayores y los dos menores
        max1 = max2 = float('-inf')
        min1 = min2 = float('inf')

    # Encuentra los dos mayores y los dos menores en el array
        for num in nums:
            if num >= max1:
                max2, max1 = max1, num
            elif num > max2:
                max2 = num

            if num <= min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num

    # Calcula el producto de los dos elementos máximos restando 1
        result = (max1 - 1) * (max2 - 1)

        return result
