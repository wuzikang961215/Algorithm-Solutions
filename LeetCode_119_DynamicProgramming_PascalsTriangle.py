class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        lastrow = [1, 2, 1]
        currentrow = 3
        while currentrow <= rowIndex:
            lastrow.append(1)
            # add number currentrow - 1 times
            for i in range(currentrow - 1):
                lastrow.append(lastrow.pop(0) + lastrow[0])
            lastrow.pop(0)
            lastrow.append(1)
            currentrow += 1
        
        return lastrow
        