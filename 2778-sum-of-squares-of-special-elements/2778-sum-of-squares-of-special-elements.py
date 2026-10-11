class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sumOfSquares = 0
        for idx, val in enumerate(nums):
            if (n % (idx+1)) == 0:
                sumOfSquares+=val**2
        return sumOfSquares

