class Solution(object):
    def minimumAbsDifference(self, arr):
        arr = sorted(arr)
        n = len(arr)
        
        min_pairs = [[arr[0],arr[1]]]
        
        for i in range(1,n-1):
            if (arr[i+1] - arr[i]) < abs(min_pairs[0][1]-min_pairs[0][0]):
                min_pairs = [[arr[i],arr[i+1]]]
            elif (arr[i+1] - arr[i]) == abs(min_pairs[0][1]-min_pairs[0][0]):
                min_pairs.append([arr[i],arr[i+1]])
            else:
                pass
            
        return min_pairs
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        