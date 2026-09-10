class Solution(object):
    def smallestSubsequence(self, s):
        last_idx = {char: i for i, char in enumerate(s)}
        stack = []
        seen = set()
        for i, char in enumerate(s):
            if char in seen:
                continue
            while stack and char < stack[-1] and i < last_idx[stack[-1]]:
                removed = stack.pop()
                seen.remove(removed)
            stack.append(char)
            seen.add(char)
            ans = ''
        for s in stack:
            ans += s
        return ans


        
        
        