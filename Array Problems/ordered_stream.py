class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.vals = [""]*n
        self.ptr = 0
        

    def insert(self, id, value):
        self.vals[id-1] = value
        
        if self.vals[self.ptr] == "":
            return []
        
        else:
            arr = []
            while(True):
                if self.ptr == self.n:
                    break
                if self.vals[self.ptr] == "":
                    break
                else:
                    arr.append(self.vals[self.ptr])
                    self.ptr += 1
            
            return arr 
        
        """
        :type id: int
        :type value: str
        :rtype: List[str]
        """
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)