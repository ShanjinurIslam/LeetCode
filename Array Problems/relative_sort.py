class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        hash_map = {}
        
        for each in arr1:
            if each in hash_map:
                hash_map[each] += 1
            else:
                hash_map[each] = 1
                
        arr = []
        
        for each in arr2:
            arr.extend([each]*hash_map[each])
        
        x = []
        
        for each in hash_map.keys():
            if each not in arr2:
                #arr.append(each)
                x.extend([each]*hash_map[each])
        
        arr.extend(sorted(x))
        return arr