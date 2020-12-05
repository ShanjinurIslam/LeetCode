class Solution(object):
    def area(self,a1,b1,a2,b2,a3,b3):
        return 0.5*abs(a1*b2 - a2*b1 + a3*b1 - a1*b3 + a2*b3 - a3*b2)
    
    def largestTriangleArea(self, points):
        n = len(points)
        
        max_area = 0
        
        for i in range(0,n-2):
            for j in range(i,n-1):
                for k in range(j,n):
                    if i!=j and j!=k:
                        a1,b1 = (points[i][0],points[i][1])
                        a2,b2 = (points[j][0],points[j][1])
                        a3,b3 = (points[k][0],points[k][1])
                        
                        max_area = max(max_area,self.area(a1,b1,a2,b2,a3,b3))
                    
        return max_area
        
        """
        :type points: List[List[int]]
        :rtype: float
        """
        