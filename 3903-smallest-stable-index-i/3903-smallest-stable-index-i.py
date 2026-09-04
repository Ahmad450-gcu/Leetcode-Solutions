class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        indices = []
        for i in range(0, n):
            list1 = nums[0:i+1]
            list2 = nums[i:n]
            if max(list1) - min(list2) <= k:
                indices.append(i)
        if len(indices) is not 0:
            return min(indices)
        return -1             
            
