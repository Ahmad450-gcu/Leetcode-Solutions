class Solution:
    def checkDivisibility(self, n: int) -> bool:
        Sum = 0
        product = 1

        for digit in str(n):
            Sum += int(digit)
            product *= int(digit)
        return True if n % (Sum + product) == 0 else False  