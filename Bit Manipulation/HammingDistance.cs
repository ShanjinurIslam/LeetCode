public class Solution {
    public int HammingDistance(int x, int y) {
        int i = 0 ;
        int diff = 0;
        
        while(i<32){
            if((x&1) != (y&1)){
                diff += 1;
            }
            
            x = x>>1;
            y = y>>1;
            
            i++ ;
        }
        
        return diff;
    }
}