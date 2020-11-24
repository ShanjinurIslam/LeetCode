class Solution(object):
    def removeDuplicates(self, S):
        stack = []
        n = len(S)
        stack.append(S[0])
        
        stack_len = 1
        
        for i in range(1,n):
            if stack_len == 0:
                stack.append(S[i])
                stack_len += 1
            else:
                if S[i] == stack[-1]:
                    stack.pop()
                    stack_len -= 1
                else:
                    stack.append(S[i])
                    stack_len += 1 
        
        final = ""
        for each in stack:
            final += str(each)
        
        return final
        
        """
        :type S: str
        :rtype: str
        """
        