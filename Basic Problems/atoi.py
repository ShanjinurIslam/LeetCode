# this is pending, could solve it

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        n = len(str)

        if n == 0:
            return 0

        if (str[0]>='0' and str[0] <='9') or str[0]=='-' :
            sum = 0
            if(str[0]=='-'):
                if n == 1:
                    return 0
                i = 1 
                while(str[i]>='0' and str[i]<='9'):
                    sum = sum*10 + (int(str[i])-int('0'))

                    if i==n-1:
                        break
                    else:
                        i += 1
                
                if sum > 2147483648:
                    return -2147483648
                else:
                    return -1*sum

            else:
                i = 0
                while(str[i]>='0' and str[i]<='9'):
                    sum = sum*10 + (int(str[i])-int('0'))
                    
                    if i==n-1:
                        break
                    else:
                        i += 1
                
                if sum > 2147483647:
                    return 2147483647
                else:
                    return sum
        else:
            return 0 


s = Solution()

print(s.myAtoi("-91283472332"))