class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        hash_map = {}
        
        hash_map[releaseTimes[0]] = [keysPressed[0]]
        
        n = len(releaseTimes)
        
        for i in range(1,n):
            val = releaseTimes[i] - releaseTimes[i-1]
            if val in hash_map:
                hash_map[val].append(keysPressed[i])
            else:
                hash_map[val] = [keysPressed[i]]
                
        
        return sorted(hash_map[max(hash_map.keys())],reverse=True)[0]
        
        
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        