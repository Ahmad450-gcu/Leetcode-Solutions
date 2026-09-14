class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ansList = [[]]
        for i in range(0, len(nums)):
            current_num = nums[i]
            current_length = len(ansList)
            for j in range(current_length):
                new_subset = ansList[j][:] 
                new_subset.append(current_num)
                ansList.append(new_subset)
        return ansList
        