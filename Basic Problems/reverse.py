class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False

        if x<0:
            negative = True

        val = abs(x)

        sum = 0
        while(val > 0):
            temp = val%10
            sum = 10*sum + temp
            val = val //10

        if negative:
            if sum > 2147483648:
                return 0 
            else:
                return -1*sum
        else:
            if sum > 2147483647:
                return 0
            else:
                return sum

        return sum


s = Solution()

print(s.reverse(-123))