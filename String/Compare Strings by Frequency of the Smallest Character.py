class Solution(object):
    def func(self,string):
        min_char = min(string)
        return string.count(min_char)
    
    def numSmallerByFrequency(self, queries, words):
        q = len(queries)
        n = len(words)
        for i in range(n):
            words[i] = self.func(words[i])
        
        for p in range(q):
            f_q = self.func(queries[p])
            count = 0
            for i in range(n):
                if f_q < words[i]:
                    count += 1
            queries[p] = count
            
        return queries
            
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        