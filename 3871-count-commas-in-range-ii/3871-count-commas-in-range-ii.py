class Solution:
    def countCommas(self, num: int) -> int:
        # strs = str(num)
        # n = len(strs)
        # if n < 4:
        #     return 0
        # if n < 7:
        #     return num - 999
        # if n < 10:
        #     return (num - 999999) + (num - 999)
        # if n < 13:
        #     return (num - 999999999) + (num - 999999) + (num - 999)
        # if n < 16:
        #     return (num - 999999999999) + (num - 999999999) + (num - 999999) + (num - 999) 
        # return (num - 999999999999) + (num - 999999999) + (num - 999999) + (num - 999) + 1 

        ans = 0
        factor = 1000
        while num >= factor:
            ans += (num - factor) + 1
            factor *= 1000
        return ans