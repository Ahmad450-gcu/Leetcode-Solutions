class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n = len (s)
        i = 0

        knowledgeMap = {}        
        for List in knowledge:
            knowledgeMap['(' + List[0] + ')'] =  List[1] 

        keysList = []
        while (i < n):
            key = ''
            if s[i] == '(':
                j = i
                while s[j] != ')':
                    key += s[j]
                    j+=1
                key += ')'
                keysList.append(key)
                i = j
            i += 1
        
        i=0
        ans = ''
        keyIdx = 0
        while (i < n):
            if s[i] == '(':
                key = keysList[keyIdx]
                keyIdx += 1
                if key in knowledgeMap:
                    ans += knowledgeMap.get(key)
                else:
                    ans += '?'
                i += len(key) - 1
            else:
                ans+=s[i]
            i+=1
        return ans
        