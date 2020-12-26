class Solution(object):
    def reformatNumber(self, number):
        number = number.replace(' ','')
        number = number.replace('-','')
        
        n = len(number)
        final = ""
        i = 0
        while(n>0):
            if (n-3 > 1) or (n%3==0):
                if i!=0:
                    final += '-'
                final += number[i:i+3]
                n -= 3
                i += 3
                continue
            if n%2 == 0:
                if i!=0:
                    final += '-'
                final += number[i:i+2]
                n -= 2
                i += 2
                continue
                
        return final
            
        
        """
        :type number: str
        :rtype: str
        """
        