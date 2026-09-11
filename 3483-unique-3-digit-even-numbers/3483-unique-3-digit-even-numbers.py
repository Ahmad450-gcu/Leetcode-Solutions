class Solution(object):
    def totalNumbers(self, digits):
        num = 100
        output = 0
        while num < 1000:
            tempList = digits[:]
            numList = []
            digitLeft = False
            numList.extend(str(num))
            for i in range(0, len(numList)):
                if int(numList[i]) in tempList:
                    tempList.remove(int(numList[i]))
                else: 
                    digitLeft = True
                    break
            if digitLeft == False:
                output += 1
            num += 2
        return output