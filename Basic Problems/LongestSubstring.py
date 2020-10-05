class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        n = len(s)

        if n < 2:
            return n

        h = {}

        i = 0 
        j = 0

        while(i<n and j<n):
            if s[j] not in h:
                h[s[j]] = 1
                j += 1
                ans = max(ans,j-i)
            else:
                del h[s[i]]
                i += 1
        
        return ans



