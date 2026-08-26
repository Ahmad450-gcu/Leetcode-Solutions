class Solution(object):
    def romanToInt(self, s):
        myDict = {
            'Z': 0,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50 ,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        total = 0
        s +='Z'
        n = len(s)
        i = 0
        while (i < n-1):
            if (myDict[s[i]] < myDict[s[i+1]]):
                total += myDict[s[i+1]] - myDict[s[i]]
                i += 2
            else: 
                total +=  myDict[s[i]]
                i += 1
        return total
            
        