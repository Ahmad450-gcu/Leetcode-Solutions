class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        originalNum = x
        reverse = 0
        while (originalNum > 0):
            digit = originalNum % 10
            reverse = (reverse*10) + digit
            originalNum //=10
        return x == reverse
        