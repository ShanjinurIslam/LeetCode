class Solution(object):
    def canFormArray(self, arr, pieces):
        hash_map = {}
        
        for i in range(len(arr)):
            hash_map[arr[i]] = i
            
        piece_wise_indexes = []
        flag = True
        
        for each in pieces:
            indexes = []
            for j in each:
                if j in hash_map:
                    indexes.append(hash_map[j])
                else:
                    flag = False
                    break
                    
            if not flag:
                break
            
            if len(indexes) == 0:
                flag = False
                break
            else:
                for i in range(len(indexes)-1):
                    if indexes[i]>indexes[i+1]:
                        flag = False
                        break
                        
                    if indexes[i+1] - indexes[i] > 1:
                        flag = False
                        break
        
        
        return flag