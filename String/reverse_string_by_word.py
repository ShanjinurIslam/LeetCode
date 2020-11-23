class Solution(object):
    def reverseWords(self, s):
        arr = s.split()
        final = ""
        
        for i in arr:
            final += i[::-1] + " "
            
        return final[:-1]
        """
        :type s: str
        :rtype: str
        """
        