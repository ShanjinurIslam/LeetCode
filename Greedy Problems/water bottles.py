class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        full_bottles = numBottles
        
        drank = 0
        previous_empty = 0
        
        while(full_bottles>0):
            
            drank += full_bottles
            
            current_empty = full_bottles + previous_empty
            
            new_bottles = current_empty/numExchange
            previous_empty = current_empty%numExchange
            
            full_bottles = new_bottles
            
        return drank
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        