from collections import defaultdict

class Solution(object):
    def letter_count_map(self,word):
        hash_map = defaultdict(int)
        
        for each in word:
            if ord(each) >= 97 and ord(each) <= 122:
                hash_map[each] += 1
        
        return hash_map
    
    def shortestCompletingWord(self, licensePlate, words):
        licensePlate = licensePlate.lower()
        lp_map = self.letter_count_map(licensePlate)
        
        min_len = 2000
        curr = words[0]
        
        for word in words:
            n = len(word)
            hash_map = self.letter_count_map(word)
            flag = True
            
            for each in lp_map.keys():
                if hash_map[each] < lp_map[each]:
                    flag = False
                    break
            
            if flag:
                if n < min_len:
                    min_len = n
                    curr = word
        
        return curr
        
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        