class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n  = len(nums)
        i = 0
        for idx, val in enumerate(nums):
            number = val
            Sum = 0
            while number > 0:
                digit = number % 10
                number = number // 10
                Sum += digit
            if Sum == idx:
                return idx
        return -1
            

            