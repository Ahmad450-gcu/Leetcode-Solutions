class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        posList = [abs(num) for num in nums]
        posList.sort()
        n = len(posList)
        if n == 1:
            return posList[0]**2
        firstHalfSum = 0
        secondHalfSum = 0
        if n % 2 == 0:
            for i in range(0, n//2):
                firstHalfSum += posList[i]**2
            for i in range(n//2, n):
                secondHalfSum += posList[i]**2 
            return secondHalfSum - firstHalfSum
        else: 
            for i in range(0, n//2):
                firstHalfSum += posList[i]**2
            secondHalfSum += posList[n//2]**2
            for i in range(n//2+1, n):
                secondHalfSum += posList[i]**2 
            return secondHalfSum - firstHalfSum
        return -1

