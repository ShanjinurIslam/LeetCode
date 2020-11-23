'''
# 64ms
class Solution(object):
    def canBeEqual(self, target, arr):
        return sorted(target) == sorted(arr)
'''
# 52 ms
class Solution(object):
    def canBeEqual(self, target, arr):
        map1 = {}
        map2 = {}
        
        n = len(target)
        
        for i in range(n):
            if target[i] in map1:
                map1[target[i]] += 1
            else:
                map1[target[i]] = 1
                
            if arr[i] in map2:
                map2[arr[i]] += 1
            else:
                map2[arr[i]] = 1
                
        for each in target:
            if each in map1 and each in map2:
                if map1[each] != map2[each]:
                    return False
            else:
                return False
            
        return True
            