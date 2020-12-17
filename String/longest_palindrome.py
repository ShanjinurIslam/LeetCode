# O(n) Solution

from collections import defaultdict

class Solution(object):
    def longestPalindrome(self, s):
        hash_map = defaultdict(int)
        
        for each in s:
            hash_map[each] += 1
            
        total = 0
        odds = []
        len_odds = 0
        
        
        for each in hash_map.keys():
            val = hash_map[each]
            if val % 2 == 0:
                total += val
            else:
                odds.append(val)
                len_odds += 1
                
        if len_odds == 0:
            return total
        
        for each in odds:
            total += each-1
        
                
        return total+1
        
        """
        :type s: str
        :rtype: int
        """
        