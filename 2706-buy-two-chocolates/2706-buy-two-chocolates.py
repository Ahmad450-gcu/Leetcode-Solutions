class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        n = len(prices)
        min1st = prices[0]
        min2nd = float('inf')
        for i in range(1, n):
            if prices[i] < min2nd and prices[i] > min1st:
                min2nd = prices[i]
            elif prices[i] <= min1st:
                min2nd = min1st
                min1st = prices[i]
            else:
                continue
        price = min1st + min2nd
        if money - price < 0:
            return money
        return money - price
