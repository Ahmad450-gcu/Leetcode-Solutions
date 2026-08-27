class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        smallest = nums[0]
        output = []
        loop = nums[-1] - nums[0]
        for i in range(1, loop):
            if smallest+i in nums:
                continue
            else:
                output.append(smallest+i)
        return output