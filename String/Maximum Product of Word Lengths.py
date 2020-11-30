class Solution(object):
    def maxProduct(self, words):
        sets = []
        
        for each in words:
            char_set = set()
            for char in each:
                char_set.add(char)
            
            sets.append(char_set)
            
        n = len(words)
        max_val = 0
        
        for i in range(0,n-1):
            for j in range(i,n):
                if sets[i] & sets[j]:
                    continue
                else:
                    max_val = max(max_val,len(words[i])*len(words[j]))
                    
        return max_val
        
        """
        :type words: List[str]
        :rtype: int
        """
        