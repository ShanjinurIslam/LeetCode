// 96ms and 26.5MB ( 71.86% time and 35.33% space)

using System.Collections.Generic;

public class Solution {
    public int OrangesRotting(int[][] grid)
        {
            Queue<Tuple<int, int>> queue = new Queue<Tuple<int, int>>();
            int n = grid.Length;
            int m = grid[0].Length;
            int[][] dist = new int[n][];
            bool[][] visited = new bool[n][];

            Tuple<int, int> start = null;
                
            int count = 0 ;
            int count_rotten = 0;
        
            for(int i = 0; i < n; i++)
            {
                dist[i] = new int[m];
                visited[i] = new bool[m];
                for (int j = 0; j < m; j++)
                {
                    
                    dist[i][j]  = int.MaxValue;
                    visited[i][j] = false;
                    if (grid[i][j] == 2)
                    {
                        dist[i][j] = 0;
                        queue.Enqueue(new Tuple<int, int>(i, j));
                        count_rotten += 1;
                    }
                    
                    if(grid[i][j] == 1){
                        count += 1;
                    }
                }
            }
        
            if(count_rotten == 0 && count == 0){
                return 0;
            }
            
            if(count_rotten == 0 && count > 0){
                return -1; 
            }
            

            int max_val = -1;
            int total_visited = 0;    
        
            while (queue.Count > 0)
            {
                Tuple<int, int> u = queue.Dequeue();
                int x = u.Item1;
                int y = u.Item2;

                if (visited[x][y])
                {
                    continue;
                }
                else
                {
                    total_visited += 1;
                    visited[x][y] = true;
                    max_val = Math.Max(dist[x][y], max_val);

                    if( x+1 < n && !visited[x+1][y] && grid[x+1][y]==1)
                    {
                        dist[x + 1][y] = Math.Min(dist[x + 1][y],dist[x][y] + 1);
                        queue.Enqueue(new Tuple<int, int>(x + 1, y));
                    }
                    if (x - 1 >= 0 && !visited[x - 1][y] && grid[x-1][y] == 1)
                    {
                        dist[x - 1][y] = Math.Min(dist[x-1][y],dist[x][y] + 1);
                        queue.Enqueue(new Tuple<int, int>(x - 1, y));

                    }

                    if (y + 1 < m && !visited[x][y+1] && grid[x][y+1] == 1 )
                    {
                        dist[x][y+1] = Math.Min(dist[x][y+1],dist[x][y] + 1);
                        queue.Enqueue(new Tuple<int, int>(x, y+1));
                    }
                    if (y - 1 >= 0 && !visited[x][y-1] && grid[x][y-1] == 1)
                    {
                        dist[x][y-1] = Math.Min(dist[x][y-1],dist[x][y] + 1);
                        queue.Enqueue(new Tuple<int, int>(x, y-1));
                    }

                    // check 4 directional condition here
                }
            }
        
            if(count != total_visited-count_rotten){
                return -1 ;
            }

            return max_val;
        }
}