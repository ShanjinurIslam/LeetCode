class Solution(object):
    def uncommonFromSentences(self, A, B):
        arr1 = A.split()
        arr2 = B.split()
        
        hash_map = {}
        
        for each in arr1:
            if each in hash_map:
                hash_map[each] += 1
            else:
                hash_map[each] = 1
                
        for each in arr2:
            if each in hash_map:
                hash_map[each] += 1
            else:
                hash_map[each] = 1
                
        arr = []
        
        for each in hash_map.keys():
            if hash_map[each] == 1:
                arr.append(each)
                
        return arr
        
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        