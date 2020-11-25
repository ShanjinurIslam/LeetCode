class Solution(object):
    def lastStoneWeight(self, stones):
        while(len(stones)>1):
            stones = sorted(stones)
            if stones[-1]!=stones[-2]:
                new = abs(stones[-1]-stones[-2])
                stones = stones[:-2]
                stones.append(new)
            else:
                stones = stones[:-2]
            
        return stones[0] if len(stones) == 1 else 0
        """
        :type stones: List[int]
        :rtype: int
        """
        