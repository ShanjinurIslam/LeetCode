class Solution(object):
    def repeatedNTimes(self, A):
        hash_map = {}
        
        final = -1
        
        for i in A:
            if i in hash_map:
                if hash_map[i] == 1:
                    final = i
                    break
            else:
                hash_map[i] = 1
                
        return final
        
        """
        :type A: List[int]
        :rtype: int
        """
        