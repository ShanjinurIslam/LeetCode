class Solution(object):
    def isPalindrome(self, x):
        a = str(x)
        b = str(a)[::-1]
        if a == b:
            return True
        else:
            return False
