class Solution(object):
    def leftRightDifference(self, nums):
        n = len(nums)
        leftSum =[0]
        rightSum =[0]
        for i in range(0, n - 1):
            answer = leftSum[i] + nums[i]
            leftSum.append(answer)
        for i in range(n - 1, 0, -1):
            answer = rightSum[n - i - 1] + nums[i]
            rightSum.append(answer)
        rightSum.reverse()
        difference = []
        for i in range(0, n):
            answer = abs(leftSum[i] - rightSum[i])
            difference.append(answer)
        return difference