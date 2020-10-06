class Solution(object):
    def printArray(self):
        s = ''
        for i in range(self.numRows):
            for j in range(len(self.arr[i])):
                if self.arr[i][j] == 0:
                    continue
                else:
                    s += self.arr[i][j]
        return s

    def convert(self, s, numRows):
        strlen = len(s)

        if(numRows == 1):
            return s

        self.numRows = numRows
        if strlen < self.numRows:
            self.numCols = strlen
        else:
            self.numCols = strlen//numRows

        self.arr = []
        for i in range(self.numRows):
            row = [0]*(self.numRows*self.numCols)
            self.arr.append(row)

        row_indices = []
        current = 0

        do_plus = True
        for _ in range(strlen):
            row_indices.append(current)
            if do_plus:
                current += 1
            else:
                current -= 1

            if current == numRows-1:
                do_plus = False

            if current == 0:
                do_plus = True

        col_indices = []
        current = 0

        count = 0

        do_flip = False

        for _ in range(strlen):
            col_indices.append(current)
            count += 1

            if numRows > 2:
                if not do_flip:
                    if count == numRows:
                        do_flip = True
                        count = 0
                        current += 1

                if do_flip:
                    if count == numRows - 2:
                        do_flip = False
                        count = 0
                        current += 1
            else:
                if numRows == 1:
                    continue
                if numRows == 2:
                    if count % 2 == 0:
                        current += 1

        count = 0
        for x, y in zip(row_indices, col_indices):
            self.arr[x][y] = s[count]
            count += 1

        return self.printArray()


print(Solution().convert("A", 2))
