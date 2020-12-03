public class Solution {
    public int NumSpecial(int[][] mat) {
        int N = mat.Length ;
        int M = mat[0].Length ;
        
        int SumOfRow(int row){
            int sum = 0;
            for(int i=0;i<M;i++){
                sum += mat[row][i];
            }
            
            return sum;
        }
        
        int SumOfCol(int col){
            int sum = 0;
            for(int i=0;i<N;i++){
                sum += mat[i][col];
            }
            
            return sum;
        }
        
        int count = 0;
        
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(mat[i][j]==1){
                    int row_sum = SumOfRow(i);
                    int col_sum = SumOfCol(j);
                    
                    if(row_sum== 1 && col_sum==1){
                        count += 1;
                    }
                }
            }
        }
        
        return count;
    }
}