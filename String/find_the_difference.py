from collections import defaultdict

class Solution(object):
    def findTheDifference(self, s, t):
        hash_map = defaultdict(int)
        
        for each in s:
            hash_map[each] += 1
            
        for each in t:
            hash_map[each] -= 1
            
        for each in hash_map.items():
            if each[1] != 0:
                return str(each[0])
        
        
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        