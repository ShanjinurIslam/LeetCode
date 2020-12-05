class Solution(object):
    def matrixReshape(self, nums, r, c):
        total = r*c
        
        n = len(nums)
        m = len(nums[0])
        
        if n*m != total:
            return nums
        
        else:
            arr = []
            
            for i in range(n):
                for j in range(m):
                    arr.append(nums[i][j])
                    
            final = []
            count = 0
            
            for i in range(r):
                final.append([])
                for j in range(c):
                    final[i].append(arr[count])
                    count += 1
            
            return final
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        