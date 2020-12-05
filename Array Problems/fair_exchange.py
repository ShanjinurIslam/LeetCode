#TLE Solution

class Solution(object):
    def fairCandySwap(self, A, B):
        alice_total = sum(A)
        bob_total = sum(B)
        
        final = []
        
        for i in A:
            for j in B:
                if (alice_total-i+j) == (bob_total-j+i):
                    final = [i,j]
                    break
                    
        return final

# Constant time Solution

class Solution(object):
    def fairCandySwap(self, A, B):
        alice_total = sum(A)
        bob_total = sum(B)
        
        setB = set(B)
        
        for x in A:
            if x + (bob_total-alice_total) / 2 in setB:
                return [x,x + (bob_total-alice_total) / 2]
        
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        