class Solution(object):
    def helper(self,val):
        stack = []
        
        curr = 0
        
        for each in val:
            if each == '#':
                if curr > 0:
                    stack.pop()
                    curr -= 1
                else:
                    continue
                    
            else:
                stack.append(each)
                curr += 1
                
        return stack,curr
    
    
    def backspaceCompare(self, S, T):
        stack_S,lenS = self.helper(S)
        stack_T,lenT = self.helper(T)
        
        return stack_S == stack_T
            
        
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        