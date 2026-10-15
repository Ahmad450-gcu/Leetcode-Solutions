class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(0, n):
            distinctSet = set()
            for j in range(i, n):
                distinctSet.add(nums[j]) 
                ans += len(distinctSet)**2
        return ans