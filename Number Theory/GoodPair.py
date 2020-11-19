class Solution(object):
    def factorial(n):
        mul = 1 
        
        for each in range(1,n+1):
            mul *= each
            
        return mul
        
    
    def numIdenticalPairs(self, nums):
        map_dict = {}
        
        for each in nums:
            if each in map_dict:
                map_dict[each] += 1
            else:
                map_dict[each] = 1
                
        
        count = 0
        
        for key in map_dict.keys():
            
        
        return 0 ;
        
        """
        :type nums: List[int]
        :rtype: int
        """
        