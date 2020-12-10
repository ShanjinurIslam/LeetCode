class Solution(object):
    def largeGroupPositions(self, s):
        ans = []
        i = 0
        for j in range(len(s)):
            if j == len(s) - 1 or s[j] != s[j+1]:
                if j-i+1 >= 3:
                    ans.append([i,j])
                i = j+1
        return ans
        """
        :type s: str
        :rtype: List[List[int]]
        """
        