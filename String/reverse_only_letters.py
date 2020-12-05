class Solution(object):
    def reverseOnlyLetters(self, S):
        stack = []
        hash_map = {}
        
        
        for i,each in enumerate(S):
            if (each >= 'a' and each <= 'z') or (each >= 'A' and each <= 'Z'):
                stack.append(each)
            else:
                hash_map[i] = each
                
        n = len(S)
        final = ""
        
        for i in range(n):
            if i in hash_map:
                final += hash_map[i]
            else:
                final += stack.pop()
                
        return final
        
        
        """
        :type S: str
        :rtype: str
        """
        