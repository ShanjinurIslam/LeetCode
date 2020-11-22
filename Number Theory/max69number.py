class Solution(object):
    def maximum69Number (self, num):
        n = num
        i = 1
        prev = 0
        max = num
        total = num
        
        while(True):
            mod = n%10
            
            if mod == 6:
                x = 9*i + prev
                x += (n/10)*(i*10) 
                
                if x > max:
                    max = x
            
            
            prev = mod*i + prev
            n = n/10
            i *= 10
            
            if n<=0:
                break
        
        return max