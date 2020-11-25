class Solution(object):
    def commonChars(self, A):
        map_arr = []
        
        for each in A:
            hash_map = {}
            
            for char in each:
                if char in hash_map:
                    hash_map[char] += 1
                else:
                    hash_map[char] = 1
            
            map_arr.append(hash_map)
            
        first = map_arr[0]
        n = len(map_arr)
        
        arr = []
        
        for each in first.keys():
            flag = True
            count = first[each]
            for i in range(1,n):
                if each in map_arr[i]:
                    count = min(count,map_arr[i][each])
                else:
                    flag = False
                    break
                
            if flag:
                arr.extend([str(each)]*count)
                
        return arr
        
        """
        :type A: List[str]
        :rtype: List[str]
        """
        