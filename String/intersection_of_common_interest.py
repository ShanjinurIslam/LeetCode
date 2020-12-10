class Solution(object):
    def findRestaurant(self, list1, list2):
        hash_map1 = {}
        hash_map2 = {}
        
        
        set1 = set()
        set2 = set()
        
        for i,each in enumerate(list1):
            hash_map1[each] = i
            set1.add(each)
            
        for i,each in enumerate(list2):
            hash_map2[each] = i
            set2.add(each)
        
        common = set1.intersection(set2)
        
        arr = []
        
        for each in common:
            arr.append((hash_map1[each]+hash_map2[each],each))
            
        arr = sorted(arr)
        min_val = arr[0][0]
        
        final = [arr[0][1]]
        
        for i in range(1,len(arr)):
            if min_val == arr[i][0]:
                final.append(arr[i][1])
            else:
                break
                
        
        return final
        
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        