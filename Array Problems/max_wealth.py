class Solution(object):
    def maximumWealth(self, accounts):
        max_val = -1 
        
        for each in accounts:
            total = sum(each)
            
            if total > max_val:
                max_val = total
                
        return max_val
        
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        