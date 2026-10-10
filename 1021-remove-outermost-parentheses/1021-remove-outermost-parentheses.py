class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        depth = 0
        ans = []
        for char in s:
            if char == '('  and depth >= 1:
                ans.append(char)
                depth += 1
            elif char == ')' and depth != 1:
                ans.append(char)
                depth -= 1
            elif char == ')' and depth == 1:
                depth = 0
            elif char == '(' and depth == 0:
                depth += 1
        return "".join(ans) 