class Solution(object):
    def heightChecker(self, heights):
        sorted_heights = sorted(heights)
        
        count = 0
        n = len(heights)
        
        for i in range(n):
            if heights[i] != sorted_heights[i]:
                count += 1
                
        return count