class Solution(object):
    def isValid(self, s):
        stack = [s[0]]
        
        for each in s[1:]:
            if len(stack) == 0:
                stack.append(each)
            elif stack[-1] == '(' and each == ')':
                stack.pop()
            elif stack[-1] == '{' and each == '}':
                stack.pop()
            elif stack[-1] == '[' and each == ']':
                stack.pop()
            else:
                stack.append(each)
                
        return True if len(stack) == 0 else False
            
        
        
        """
        :type s: str
        :rtype: bool
        """
        