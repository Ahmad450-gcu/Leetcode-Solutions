class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ansList = []
        ansTuppleList = []
        nums.sort()
        n = len(nums)
        for idx,num in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            l = idx + 1 
            r = n - 1
            while l < r:
                Sum = num+nums[l]+nums[r]
                if Sum == 0:
                    ansList.append([num,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif Sum < 0:
                    l += 1
                elif Sum > 0:
                    r -= 1
        
        return ansList         
        