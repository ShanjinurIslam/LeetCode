class Solution(object):
    def uniqueOccurrences(self, arr):
        map1 = {}
        
        for i in arr:
            if i in map1:
                map1[i] += 1
            else:
                map1[i] = 1
        
        map2 = {}
        
        for i in map1.keys():
            if map1[i] in map2:
                return False
            else:
                map2[map1[i]] = 1
                
        return True