class Solution(object):
    def sum_digit(self,num):
        sum = 0
        while(num>0):
            sum += num%10
            num = num // 10
        
        return sum
    
    def addDigits(self, num):
        while(num//10 != 0):
            num = self.sum_digit(num)
            
        return num
        
        """
        :type num: int
        :rtype: int
        """
        