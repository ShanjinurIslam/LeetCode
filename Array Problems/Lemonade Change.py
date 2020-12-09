class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        hash_map = {}
        
        hash_map[5] = 0
        hash_map[10] = 0
        hash_map[20] = 0
        
        for bill in bills:
            print(hash_map)
            
            if bill == 5:
                hash_map[5] += 1
            elif bill == 10:
                if hash_map[5] >= 1:
                    hash_map[5] -= 1
                    hash_map[10] += 1
                else:
                    return False
            else:
                if (hash_map[5] >= 1 and hash_map[10] >= 1):
                    hash_map[5] -= 1
                    hash_map[10] -= 1
                    hash_map[20] += 1
                elif hash_map[5] >= 3:
                    hash_map[5] -= 3
                    hash_map[20] += 1
                else:
                    return False
                
        return True