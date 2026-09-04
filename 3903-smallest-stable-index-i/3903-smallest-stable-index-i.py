# class Solution:
    # def firstStableIndex(self, nums: list[int], k: int) -> int:
    #     n = len(nums)
    #     indices = []
    #     for i in range(0, n):
    #         list1 = nums[0:i+1]
    #         list2 = nums[i:n]
    #         if max(list1) - min(list2) <= k:
    #             indices.append(i)
    #     if len(indices) is not 0:
    #         return min(indices)
    #     return -1
# I originially did it as above. But the above approach takes 0(N^2) as we are finding min and max inside the loop in each iteration. A better way to do it is to first calculate all the suffix minimums and then update a variable to hold the maximum until index i and then simply subtract suffixMin[i] from it, if it is less than k, return index immediately as it will be for sure the smallest stable index as we are iterating in the forward direction where the next index is always greater than previous.
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
            
