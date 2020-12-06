from math import ceil

class Solution(object):
    def checkIfExist(self, arr):
        hash_map = {}
        flag = False
        
        
        for each in arr:
            if int(each*2) in hash_map:
                flag = True
                break
                
            if each//2 in hash_map and each%2 ==0:
                flag = True
                break
            
            hash_map[int(each)] = 1
        
        return flag