class Solution(object):
    def produce_range(self,arr,s,e):
        if s == e:
            return 
        else:
            length = e-s 
            c = 1
            for i in range(s,s+length/2):
                arr[i] = c
                c += 1
            
            if (e-s) % 2 == 0:
                c -= 1
                
            for i in range(s+length/2,e):
                arr[i] = c
                c -= 1   
            
            return
        
    
    def find_indexes(self,string,char):
        indexes = []
        
        for i,each in enumerate(string):
            if each == char:
                indexes.append(int(i))
                
        return indexes
                    
    
    def shortestToChar(self, S, C):
        arr = [0]*len(S)
        
        indexes = self.find_indexes(S,C)
        n = len(indexes)
        
        # first
        c = 0
        for i in range(indexes[0],-1,-1):
            arr[i] = c
            c += 1
        
        
        for i in range(0,n-1):
            self.produce_range(arr,indexes[i]+1,indexes[i+1])
        
        c = 1
        # final
        for i in range(indexes[-1]+1,len(S)):
            arr[i] = c
            c += 1
        
        
        return arr
        
        
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        