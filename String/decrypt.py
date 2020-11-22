class Solution(object):
    def freqAlphabets(self, s):
        indexes = []
        final = ""
        
        strlen = len(s)
        
        for i in range(strlen):
            if s[i] == '#':
                indexes.append(i)
                
        if(len(indexes)>0):
            curr = 0
            for each in indexes:
                x = s[curr:each]
                n = len(x)
                
                for c in x[0:n-2]:
                    final += str(chr(ord('a') + int(c) - 1))
                    
                final += str(chr(ord('a') + int(x[n-2:]) -1))
                curr = each+1
                
            if(indexes[-1]<strlen):
                for each in s[indexes[-1]+1:]:
                    final += str(chr(48+ord(each)))
            
        else:
            for each in s:
                final += str(chr(48+ord(each)))
            
        return final