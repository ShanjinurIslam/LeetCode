from collections import defaultdict

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        found = defaultdict(int)
        
        for each in dominoes:
            s1 = (each[0],each[1])
            s2 = (each[1],each[0])
            
            if s1 in found:
                found[s1] += 1
                continue
            elif s2 in found:
                found[s2] += 1
            else:
                found[s1] = 1
        
        count = 0
        
        for each in found.keys():
            val = found[each]
            if val>1:
                count += (val*(val-1))//2 # n Choose 2
            
        return count
        
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        