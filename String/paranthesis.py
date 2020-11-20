class Solution(object):
    def removeOuterParentheses(self, S):
        depth = 0
        out = ""

        n = len(S)
        
        for i in range(n):
            if S[i] == "(":
                if depth >= 1:
                    out += S[i]
                
                depth += 1
            else:
                if depth > 1:
                    out += S[i]
                
                depth -= 1
                
        return out
                