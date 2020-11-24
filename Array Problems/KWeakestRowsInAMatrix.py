class Solution(object):
    def kWeakestRows(self, mat, k):
        hash_map = {}
        
        n = len(mat)
        
        for i in range(n):
            hash_map[i] = (mat[i].count(1),i)
            
        
        return [x[1] for x in sorted(hash_map.values())[:k]]
        
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        