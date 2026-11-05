class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        moves = 0
        for i in range(n-1, 0, -1):
            moves += nums[i] - nums[0]
        return moves