class Solution(object):
    def numJewelsInStones(self, J, S):
        diff = {}
        
        for each in S:
            if each in diff:
                diff[each] += 1
            else:
                diff[each] = 1
                
        total = 0
        
        for each in J:
            if each in diff:
                total += diff[each]
                
        return total 
        