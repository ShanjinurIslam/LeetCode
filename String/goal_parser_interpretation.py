class Solution(object):
    def interpret(self, command):
        stack = []
        n = len(command)
        i = 0 
        while(i<n):
            each = command[i]
            if len(stack) == 0:
                stack.append(each)
            elif stack[-1] == '(' and each == ')':
                stack.pop()
                stack.append('o')
            elif stack[-1] == '(' and each == 'a':
                stack.pop()
                stack.append('a')
                stack.append('l')
                i = i+2
            else:
                stack.append(each)
                    
            i += 1
        
        return ''.join(stack)
                
        """
        :type command: str
        :rtype: str
        """
        