class Solution:
    def countAndSay(self, n: int) -> str:
        def countFrequency(string: str):
            numFreq = []
            n = len(string)  
            i = 0
            freq = 0
            while i < n:
                if i != 0 and string[i] == string[i-1]:
                    freq += 1
                elif i != 0 and string[i] != string[i-1]:
                    numFreq.append([str(freq), string[i-1]])
                    freq = 1
                else:
                    freq += 1
                i += 1 
            numFreq.append([str(freq), string[-1]])
            return numFreq
        
        ans = '1'
        for i in range(1, n):
            currList = countFrequency(ans)
            ans2 = ''
            for l in currList:
                freq = l[0]
                num = l[1]
                ans2 += freq + num
            ans = ans2
        return ans