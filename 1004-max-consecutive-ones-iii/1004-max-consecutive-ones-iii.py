class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        zeroCount = 0
        maxLen = 0
        for right in range(0, len(nums)):
            if (nums[right] == 0): 
                zeroCount+=1;           
            while zeroCount > k:
                if (nums[left] == 0): 
                    zeroCount-=1
                left+=1
            maxLen = max(maxLen, right - left + 1)
        return maxLen
        