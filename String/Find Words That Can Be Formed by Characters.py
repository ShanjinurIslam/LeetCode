class Solution(object):
    def countCharacters(self, words, chars):
        hash_map = {}
        
        for char in chars:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1
              
        total = 0
        
        for word in words:
            word_map = {}
            n = len(word)
            
            for char in word:
                if char in word_map:
                    word_map[char] += 1
                else:
                    word_map[char] = 1
            flag = True
            
            for key in word_map.keys():
                if key in hash_map and hash_map[key] >= word_map[key]:
                    pass
                else:
                    flag = False
                    break
            
            if flag:
                total += n
            else:
                continue
                
        return total
        
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        