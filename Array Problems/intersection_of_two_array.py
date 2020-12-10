class Solution(object):
    def intersect(self, nums1, nums2):
        hash_map1 = {}
        hash_map2 = {}
        
        for each in nums1:
            if each in hash_map1:
                hash_map1[each] += 1
            else:
                hash_map1[each] = 1
        
        for each in nums2:
            if each in hash_map2:
                hash_map2[each] += 1
            else:
                hash_map2[each] = 1
        
        
        intersecting_keys = set(list(hash_map1.keys())).intersection(list(hash_map2.keys()))
        
        arr = []
        
        for each in intersecting_keys:
            arr.extend([each]*min(hash_map1[each],hash_map2[each]))
        
        
        return arr
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        