class Solution(object):
    def sortString(self, s):
        hash_map = {}
        
        str_len = len(s)
        
        for i in s:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
                
        alphabets = list(sorted(hash_map.keys()))
        
        final_string = ""
        cur = 0
        
        while(True):
            for each in alphabets:
                if hash_map[each] > 0:
                    hash_map[each] -= 1
                    final_string += str(each)
                    cur += 1
                    
            for each in reversed(alphabets):
                if hash_map[each] > 0:
                    hash_map[each] -= 1
                    final_string += str(each)
                    cur += 1
                    
            if cur == str_len:
                break
        
        return final_string
        