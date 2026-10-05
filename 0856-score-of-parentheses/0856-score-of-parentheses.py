class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        stack = []
        score = 0
        for i in range(0,n):
            if s[i] == '(': 
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(2*score, 1)
        return score