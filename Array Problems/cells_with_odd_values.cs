public class Solution {
    public int OddCells(int n, int m, int[][] indices) {
        int[,] matrix = new int[n,m] ;
        
        for(int i=0;i<indices.Length;i++){
            int[] pair = indices[i];
            
            
            for(int x=0;x<n;x++){
                matrix[x,pair[1]] += 1 ;
            }
            for(int y=0;y<m;y++){
                matrix[pair[0],y] += 1 ;
            }
        }
        
        int count = 0;
        
        for(int p=0;p<n;p++){
            for(int q=0;q<m;q++){
                if(matrix[p,q]%2!=0){
                    count += 1 ;
                }
            }
        }
        
        return count;
    }
}