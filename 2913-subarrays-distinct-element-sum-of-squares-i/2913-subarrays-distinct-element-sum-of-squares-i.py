class Solution:
    def sumCounts(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0
        for i in range(0, n):
            for j in range(i+1, n+1):
                li = nums[i:j]
                distinctCount = len(set(li))
                ans += distinctCount**2
        return ans