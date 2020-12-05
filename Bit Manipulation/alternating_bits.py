class Solution(object):
    def hasAlternatingBits(self, n):
        binary = bin(n)
        
        flag = True
        
        for i in range(0,len(binary)-1):
            if binary[i] == binary[i+1]:
                flag = False
                break
                
        return flag
            
        
        """
        :type n: int
        :rtype: bool
        """
        