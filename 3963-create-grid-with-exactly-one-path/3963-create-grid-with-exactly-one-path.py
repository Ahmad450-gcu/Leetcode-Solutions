class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        myList = []
        # row = 1
        
        # while row <= m:
        #     currRowPath = ''
        #     col = 1
        #     if row == 1:
        #         currRowPath += '.'*n
        #         myList.append(currRowPath)
        #         row += 1
        #         continue
        #     while col < n:
        #         currRowPath+='#'
        #         col += 1
        #     currRowPath+='.'
        #     myList.append(currRowPath)
        #     row += 1
        # return myList

        topRow = '.'*n
        belowRemainingRows = '#' * (n-1) + '.'
        return [topRow] + [belowRemainingRows] * (m-1)