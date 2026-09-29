class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = len(strs)
        longestPrefix = strs[0]
        for i in range(1, n):
            j = 0
            currPrefix = ''
            while (j < len(strs[i]) and j < len(longestPrefix)):
                if strs[i][j] == longestPrefix[j]:
                    currPrefix += longestPrefix[j]
                    j+=1
                else: 
                    break
            longestPrefix = currPrefix
        return longestPrefix
                