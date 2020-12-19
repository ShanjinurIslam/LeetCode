class Solution(object):
    def convertToBase7(self, num):
        flag = True
        
        if num == 0:
            return "0"
        
        if num < 0:
            flag = False
        
        num = int(abs(num))
        
        stack = []
        n = 0
        
        while(num>=1):
            div = num%7
            num = num//7
            stack.append(div)
            n += 1
        
        string = ""
        
        while(n>0):
            string += str(stack.pop())
            n -= 1
        return string if flag else ("-"+string)
        
        """
        :type num: int
        :rtype: str
        """
        