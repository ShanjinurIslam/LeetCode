class Solution(object):
    def get_digits(self, n):
        hash_map = {}
        
        while(n>0):
            x = n%10
            n = n/10
            
            if x in hash_map:
                continue
            else:
                hash_map[x] = 1
            
        return list(hash_map.keys())
    
    def divisibility(self,n,arr):
        flag = True
        
        for i in arr:
            if n % i != 0:
                flag = False 
                break
                
        return flag
    
    
    def selfDividingNumbers(self, left, right):
        arr = []
        for i in range(left,right+1):
            if i % 10 == 0:
                continue
            else:
                digits = self.get_digits(i)
                if 0 in digits:
                    continue
                
                else:
                    if self.divisibility(i,digits) == True:
                        arr.append(i)
                    
        return arr