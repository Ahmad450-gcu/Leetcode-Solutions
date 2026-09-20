class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = -1
        for i, char in enumerate(s):
            output += (i + 1) *  (27 - (ord(char) - 96)) 
        return output + 1