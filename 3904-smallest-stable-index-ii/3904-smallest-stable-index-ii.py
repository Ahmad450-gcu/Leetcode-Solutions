class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffixMin = [0] * n
        suffixMin[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i+1])
        currMax = -1
        for i in range(0, n):
            if nums[i] > currMax:
                currMax = nums[i]
            if currMax - suffixMin[i] <= k:
                return i
        return -1