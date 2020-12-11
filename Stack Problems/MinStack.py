import random
import bisect

class MinStack(object):
    def binary_search(self,val):
        s = 0
        e = self.n - 1
        
        while(s<=e):
            mid = (s+e)/2
            
            if self.ll[mid] == val:
                return mid
            elif self.ll[mid] < val:
                s = mid + 1
            else:
                e = mid - 1
                
        return -1

    def __init__(self):
        self.n = 0
        self.list = []
        self.ll = []

    def push(self, x):
        self.n += 1
        self.list.append(x)
        bisect.insort(self.ll,x)

    def pop(self):
        val = self.top()
        self.list.pop()
        
        index = self.binary_search(val)
        
        self.ll.pop(index)
        
        self.n -= 1
        
    def top(self):
        return self.list[-1]

    def getMin(self):
        return self.ll[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()