class Solution(object):
    def isValid(self, s):
        n = len(s)
        stack = []
        stack.append(s[0])
        for i in range (1, n):
            if (len(stack)):
                if ((stack[-1] == "(" and s[i] == ")") or (stack[-1] == "{" and s[i] == "}") or (stack[-1] == "[" and s[i] == "]")):
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return False if stack else True