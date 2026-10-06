class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
        return len(stack)