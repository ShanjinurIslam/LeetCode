# DP Solution

# Approach

'''
Consider Alice's Turn = True and Bob's Turn = False

For instance, N = 3 so valid x values would be 1

Let's consider x = 1 then N -> 2 and Turn -> False

For N -> 2 valid x = 1
x = 1 , N becomes 1 and Turn -> True

if N == 1 and Turn == True: then alice can't win

'''

class Solution(object):
    def divisorGame(self, N):
        calculated = [-1]*(N+1)
        arr = [False]*(N+1)
        
        def subproblem(N,turn):
            if calculated[N] != -1:
                return arr[N]
            else:
                if turn == True and N == 1:
                    return False
                
                if turn == False and N == 1:
                    return True
                else:
                    for i in range(1,N):
                        if N % i == 0:
                            arr[N] |= subproblem(N-i,not turn) 
        
                calculated[N] = 1
                
                return arr[N]
                
        
        return subproblem(N,True)
        
        """
        :type N: int
        :rtype: bool
        """
        