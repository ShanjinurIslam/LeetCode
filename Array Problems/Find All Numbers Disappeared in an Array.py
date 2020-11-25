class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        
        arr = [0]*n
        
        for each in nums:
            arr[each-1] += 1
            
        final = []   
            
        for i in range(n):
            if arr[i] == 0:
                final.append(i+1)
                
        return final
        
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        