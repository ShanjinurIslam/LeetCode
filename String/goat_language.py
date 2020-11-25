class Solution(object):
    def convert(self,string,index):
        vowels = {'a','e','i','o','u'}
        
        if string[0].lower() in vowels:
            return string + "ma" + "a"*index
        else:
            return string[1:] + string[0] + "ma" + "a"*index
            
    
    def toGoatLatin(self, S):
        strings = S.split()
        
        final = ""
        
        for i,each in enumerate(strings):
            final += self.convert(each,i+1) + " "
            
        return final[:-1]
        
        """
        :type S: str
        :rtype: str
        """
        