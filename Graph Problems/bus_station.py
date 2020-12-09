# ac on 36/37 case last case tle :-) 

class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        edgeList = []
        
        n = len(distance)
        i = 0
        
        for each in distance:
            edgeList.append((i,(i+1)%n,each))
            edgeList.append(((i+1)%n,i,each))
            i += 1
        
        
        dist = [10e10]*n
        dist[start] = 0
        
        for _ in range(0,n):
            for edge in edgeList:
                (a,b,w) = edge
                
                dist[b] = min(dist[b],dist[a]+w)
        
        return dist[destination]

# linear time solve

class Solution(object):
    def clock_wise_seq(self,n,s,d):
        arr = [s]
        
        while(s!=d):
            arr.append((s+1)%n)
            s = (s+1)%n
            
        return arr
    
    def anticlock_wise_seq(self,n,s,d):
        arr = [s]
        
        while(s!=d):
            if s == 0:
                s = n
            
            arr.append(s-1)
            s = (s-1)
            
        return arr
    
    def distanceBetweenBusStops(self, distance, start, destination):
        n = len(distance)
        
        weight = {}
        i = 0
        
        for each in distance:
            weight[(i,(i+1)%n)] = each
            weight[((i+1)%n,i)] = each
            
            i = (i+1)%n
            
        
        clk = self.clock_wise_seq(n,start,destination)
        anti = self.anticlock_wise_seq(n,start,destination)
        
        total_clk = 0
        total_anti = 0
        
        for i in range(len(clk)-1):
            total_clk += weight[clk[i],clk[i+1]]
        
        for i in range(len(anti)-1):
            total_anti += weight[anti[i],anti[i+1]]
            
        min_val = min(total_clk,total_anti)
        
        return min_val
        
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        