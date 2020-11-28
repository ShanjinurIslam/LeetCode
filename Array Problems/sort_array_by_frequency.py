class Solution(object):
    def frequencySort(self, nums):
        hash_map = {}
        
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        
        count_map = {}
        
        for key in hash_map.keys():
            if hash_map[key] in count_map:
                count_map[hash_map[key]].append(key)
            else:
                count_map[hash_map[key]] =[key]
            
        arr = sorted(count_map.keys())
        
        final = []
        
        for each in arr:
            temp = sorted(count_map[each],reverse=True)
            for x in temp:
                final.extend([x]*each)
            
        return final
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        