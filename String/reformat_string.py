class Solution(object):
    def reformat(self, s):
        number_queue = []
        letter_queue = []
        
        for each in s:
            if ord(each) >= 48 and ord(each) <= 57:
                number_queue.append(each)
            else:
                letter_queue.append(each)
                
        m = len(number_queue)
        n = len(letter_queue)
        
        if abs(m-n) <= 1:
            final = ""
            turn = 0
            
            if m > n:
                first = number_queue
                second = letter_queue
            else:
                first = letter_queue
                second = number_queue
            
            
            while((len(first) + len(second)) > 0):
                if turn % 2 == 0:
                    final += first.pop(0)
                else:
                    final += second.pop(0)
                    
                turn += 1
                    
            return final
        else:
            return ""
        """
        :type s: str
        :rtype: str
        """
        