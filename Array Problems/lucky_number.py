from collections import defaultdict

class Solution(object):
    def findLucky(self, arr):
        hash_map = defaultdict(int)
        
        for each in arr:
            hash_map[each] += 1
            
        final = []  
            
        for each in hash_map.keys():
            if each == hash_map[each]:
                final.append(each)
                
        return sorted(final,reverse=True)[0] if len(final) >= 1 else -1
        
        """
        :type arr: List[int]
        :rtype: int
        """
        