class Solution(object):
    def judgeCircle(self, moves):
        pos = [0,0]
        
        for i in moves:
            if i == 'U':
                pos[1] += 1
            elif i == 'D':
                pos[1] -= 1
            elif i == 'L':
                pos[0] -= 1
            else:
                pos[0] += 1
                
        if pos[0] == 0 and pos[1] == 0:
            return True
        else:
            return False