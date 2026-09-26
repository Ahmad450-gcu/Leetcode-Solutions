class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n = len (s)
        knowledgeMap = {}
        
        for List in knowledge:
            knowledgeMap['(' + List[0] + ')'] =  List[1] 

        keysList = []

        for i in range(0, n):
            key = ''
            if s[i] == '(':
                j = i
                while s[j] != ')':
                    key += s[j]
                    j+=1
                key += ')'
                keysList.append(key)
                i = j
        
        for key in keysList:
            if key in knowledgeMap:
                s = s.replace(key,  knowledgeMap.get(key))
            else:
                s = s.replace(key, '?')
        return s