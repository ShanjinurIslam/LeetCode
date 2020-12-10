from functools import reduce

class Solution(object):
    def factors(self,n):    
        return list(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    def constructRectangle(self, area):
        f = self.factors(area)
        
        final_L = area
        final_W = 1
        
        for L in f[::-1]:
            W = area/L
            
            if (L<W):
                continue
            else:
                if abs(L-W) < abs(final_L-final_W):
                    final_L = L
                    final_W = W
        
        return [final_L,final_W]
        
        
        """
        :type area: int
        :rtype: List[int]
        """
        