class Solution(object):
    def countBits(self, num):
        return [bin(each).count('1') for each in range(0,num+1)]
        """
        :type num: int
        :rtype: List[int]
        """
        