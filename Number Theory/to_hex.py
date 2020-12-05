class Solution(object):
    def hex_map(self,val):
        hash_map = {}
        
        hash_map[0] = '0'
        hash_map[1] = '1'
        hash_map[2] = '2'
        hash_map[3] = '3'
        hash_map[4] = '4'
        hash_map[5] = '5'
        hash_map[6] = '6'
        hash_map[7] = '7'
        hash_map[8] = '8'
        hash_map[9] = '9'
        hash_map[10] = 'a'
        hash_map[11] = 'b'
        hash_map[12] = 'c'
        hash_map[13] = 'd'
        hash_map[14] = 'e'
        hash_map[15] = 'f'
        
        return hash_map[val]
    
    def toHex(self, num):
        
        if num < 0:
            num = int(1 << 32) - abs(num)
        
        if num == 0:
            return '0'
        
        stack = []
        
        while(num!=0):
            mod = num % 16
            num = num // 16
            stack.append(self.hex_map(mod))
            
        final = ""
        
        while(len(stack)>0):
            final += stack.pop()
        
        return final
        
        """
        :type num: int
        :rtype: str
        """
        