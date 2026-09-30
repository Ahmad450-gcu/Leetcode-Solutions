class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        stack = []
        ans = []
        for s in seq:
            if s == '(':
                ans.append(len(stack) %2)
                stack.append('(')
            elif s == ')':
                stack.pop()
                ans.append(len(stack)%2)
        return ans