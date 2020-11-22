from math import ceil
import random

class Solution(object):
    def get_all_odds(self,n):
        odds = []
        
        for i in range(1,n+1):
            if i%2 == 0:
                continue
            else:
                odds.append(i)
                
        return sorted(odds,reverse=True)
    
    def generateTheString(self, n):
        odds = self.get_all_odds(n)
        string = ""
        chars = "abcdefghijklmopqrstuvwxyz"
        count = 0
        x = n
        
        string = ""
        
        while(True):
            for char in chars:
                for odd in odds:
                    if int(x/odd) != 0 and count<n:
                        string += odd*str(char)
                        count += odd
                        x -= odd
                        break
            if count == n:
                break
        
        return string
