class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)
        ways = [0] * (n+1)
        ways[0] = 1
        for char in s:
            for j in range(n, 0, -1):
                if char == t[j-1]:
                    ways[j] += ways[j-1]
        return ways[n]
