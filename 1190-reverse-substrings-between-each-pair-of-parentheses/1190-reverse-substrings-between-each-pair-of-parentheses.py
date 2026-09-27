class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        wordStack = []
        ans = ''
        i = 0
        while i < n:
            if s[i] != ')':
                wordStack += s[i]
                i+=1
            elif s[i] == ')':
                tempWord = ''
                while wordStack and wordStack[-1] != '(':
                    tempWord += wordStack.pop()
                wordStack.pop()
                wordStack += tempWord
                i+=1
        return ''.join(wordStack)
       
