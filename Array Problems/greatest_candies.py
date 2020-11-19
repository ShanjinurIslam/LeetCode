class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        max_val = max(candies)
        verdict = []
        
        for each in candies: 
            if each+extraCandies >= max_val:
                verdict.append(True)
            else:
                verdict.append(False)
                
        return verdict 