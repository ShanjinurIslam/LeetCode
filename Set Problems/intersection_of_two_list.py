class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set()
        set2 = set()
        
        for num in nums1:
            set1.add(num)
            
        for num in nums2:
            set2.add(num)
            
        return list(set1.intersection(set2))
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        