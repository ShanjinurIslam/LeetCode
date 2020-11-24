class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        i = 0
        sum = 0
        
        while i<32:
            sum = (sum<<1) | (n & 1)
            n = n >> 1 
            i += 1
            
        return sum
            