class Solution(object):
    def sortArrayByParityII(self, A):
        n = len(A)
        odd = []
        even = []
        
        for each in A:
            if each % 2 == 0:
                even.append(each)
            else:
                odd.append(each)
                
        final = [0]*n    
                
        for i in range(n/2):
            final[2*i+1] = odd[i]
            final[i*2] = even[i]
            
        return final
        
        """
        :type A: List[int]
        :rtype: List[int]
        """
        