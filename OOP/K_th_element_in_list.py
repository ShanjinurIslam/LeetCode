import bisect # maintains a sorted list
 
class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.list = []
        self.n = 0
        
        for val in nums:
            bisect.insort(self.list,val)
            self.n += 1
        

    def add(self, val):
        bisect.insort(self.list,val)
        self.n += 1
        return self.list[self.n-self.k]
        """
        :type val: int
        :rtype: int
        """
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)