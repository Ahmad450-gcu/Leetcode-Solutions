class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)
        if n == 1:
            return 1
        minimum = min(nums)
        min_idx = nums.index(minimum)
        maximum = max(nums)
        max_idx = nums.index(maximum)
        if ((min_idx <= n//2) and (max_idx <= n//2)):
            return (max(min_idx, max_idx)+1)
        if ((min_idx >= n//2) and (max_idx >= n//2)):
            return (n - min(min_idx, max_idx))
        bigger = max(min_idx, max_idx)
        smaller = min(min_idx, max_idx) 
        con1 = bigger + 1
        con2 = n - smaller
        con3 = (smaller+1)+(n - bigger)
        return min(con1, con2, con3)