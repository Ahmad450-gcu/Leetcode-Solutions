class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)
        num_set = set(nums)
        Break = False
        i = 1
        ans = 0
        while (Break == False):
            if (k * i) in num_set:
                i+=1
            else:
                ans = k*i
                Break = True
        return ans