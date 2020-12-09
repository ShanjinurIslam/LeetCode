from math import ceil

class Solution(object):
    def countOdds(self, low, high):
        if high % 2 ==0 and low % 2 == 0:
            return high//2 - low//2
        
        elif high%2 != 0 and low % 2 == 0:
            return high//2 - low//2 + 1
        
        elif high%2 == 0 and low % 2 != 0:
            return high//2 - low//2
        else:
            return high//2 - low//2 + 1
        
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        