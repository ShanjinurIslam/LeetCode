from collections import defaultdict

# detect cycle in number order

class Solution(object):
    def get_digit_squared_sum(self,n):
        sum = 0
        
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        while(n>0):
            sum += (n%10)**2
            n = n/10
            
        return sum
    
    
    def isHappy(self, n):
        hash_map = defaultdict(int)
        
        prev = n
        hash_map[prev] = 1
        
        while(n!=1):
            n = self.get_digit_squared_sum(prev)
            
            hash_map[n] += 1
            
            if hash_map[n] > 1:
                break
            else:
                prev = n
            
        return True if hash_map[1] != 0 else False
        
        """
        :type n: int
        :rtype: bool
        """
        