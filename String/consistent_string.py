class Solution(object):
    def countConsistentStrings(self, allowed, words):
        found = dict()
        
        for each in allowed:
            found[each] = 1
        
        count = 0
        for word in words:
            flag = True
            
            for char in word:
                if not char in found:
                    flag = False
                    break
            
            if flag:
                count += 1
        return count
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        