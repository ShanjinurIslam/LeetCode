class Solution(object):
    def generate_sieve(self,n):
        sieve = [0]*(1+n)
        for x in range(2,n+1):
            if sieve[x] != 0:
                continue
            for u in range(2*x,n+1,x):
                sieve[u] = x
                
        return sieve
    
    def countPrimeSetBits(self, L, R):
        sieve = self.generate_sieve(25)
        count = 0
        
        for i in range(L,R+1):
            set_bits = bin(i).count('1')
            if set_bits != 0 and set_bits != 1:
                if sieve[set_bits] == 0:
                    count += 1
        
        return count