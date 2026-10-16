class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans = ''
        while ((len(ans) < num) and sum > 0):
            if sum > 9:
                ans += '9'
                sum -= 9
            else:
                ans += str(sum)
                sum = 0
        if sum > 0:
            return ''
        while len(ans) < num:
            ans += '0'
        return ans