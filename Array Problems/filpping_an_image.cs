public class Solution {
    public int[][] FlipAndInvertImage(int[][] A) {
        int n = A.Length ;
        
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                int temp = A[i][n-1-j];
                A[i][n-1-j] = A[i][j];
                A[i][j] = temp;
            }
        }
        
        
        
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(A[i][j]==0){
                    A[i][j] = 1 ;
                }
                else{
                    A[i][j] = 0 ;
                }
            }
        }
        
        return A;
    }
}