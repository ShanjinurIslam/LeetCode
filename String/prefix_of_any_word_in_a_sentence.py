class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        n = len(searchWord)
        words = sentence.split()
        
        for i,each in enumerate(words):
            if len(each) >= n:
                if each[:n] == searchWord:
                    return i+1
        return -1
        
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        