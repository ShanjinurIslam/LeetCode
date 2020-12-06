class Solution(object):
    def create_row(self, index):
        return [-1]*index
    
    def getRow(self, rowIndex):
        arr = []
        
        for i in range(0,rowIndex+1):
            row = self.create_row(i+1)
            row[0] = 1
            row[-1] = 1
            arr.append(row)
        
        for level in range(2,rowIndex+1):
            for index in range(1,level):
                arr[level][index] = arr[level-1][index-1] + arr[level-1][index]
        
        return arr[rowIndex]
        
        
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        