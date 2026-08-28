class Solution(object):
    def sumAndMultiply(self, s, queries):
        m = len(s)
        MOD = 10**9 + 7
        power10 = [1] * (m + 1)
        for i in range(1, m + 1):
            power10[i] = (power10[i - 1] * 10) % MOD
        prefixNonZeros = [0] * (m + 1)
        prefixSum = [0] * (m + 1)
        prefixNum = [0] * (m + 1)
        for i in range(m):
            digit = int(s[i])
            if digit > 0:
                prefixNonZeros[i + 1] = prefixNonZeros[i] + 1
                prefixSum[i + 1] = prefixSum[i] + digit
                prefixNum[i + 1] = (prefixNum[i] * 10 + digit) % MOD
            else:
                prefixNonZeros[i + 1] = prefixNonZeros[i]
                prefixSum[i + 1] = prefixSum[i]
                prefixNum[i + 1] = prefixNum[i]          
        output = []
        for l, r in queries:
            rangeSum = prefixSum[r + 1] - prefixSum[l]
            digits_in_range = prefixNonZeros[r + 1] - prefixNonZeros[l]
            nonZero = (prefixNum[r + 1] - (prefixNum[l] * power10[digits_in_range])) % MOD
            product = (nonZero * rangeSum) % MOD
            output.append(product)
        return output