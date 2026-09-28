class Solution:
    def maxDepth(self, s: str) -> int:
        currDepth = 0
        maxDepth = 0
        n = len(s)
        for i in range (0,n):
            if s[i] == '(':
                currDepth += 1
            elif s[i] == ')':
                currDepth -=1
            maxDepth = max(maxDepth,currDepth)
        return maxDepth  