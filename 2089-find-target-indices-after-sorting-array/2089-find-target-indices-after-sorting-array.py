from collections import Counter
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        if target not in nums:
            return []
        else:
            start = nums.index(target)
        indiceList = []
        
        while start < len(nums) and nums[start] == target:
            indiceList.append(start)
            start += 1
        return indiceList
        