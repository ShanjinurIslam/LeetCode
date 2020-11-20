class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        cost = 0
        
        n = len(points)
        
        for i in range(0,n-1):
            point_a = points[i]
            point_b = points[i+1]
            
            dist_x =  abs(point_b[0] - point_a[0])
            dist_y =  abs(point_b[1] - point_a[1])
            
            if dist_x < dist_y :
                cost += dist_x
                dist_y -= dist_x
                cost += dist_y
            elif dist_x == dist_y:
                cost += dist_x
            else:
                cost += dist_y
                dist_x -= dist_y
                cost += dist_x
    
        return cost
        
        """
        :type points: List[List[int]]
        :rtype: int
        """
        