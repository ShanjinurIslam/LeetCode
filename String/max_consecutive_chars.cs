public class Solution {
    public int MaxPower(string s) {
        int count = 1;
        int total = 1;
        for(int i=1;i<s.Length;i++){
            if(s[i-1]==s[i]){
                count += 1;
                total = Math.Max(total,count) ;
            }
            else{
                count = 1;
            }
        }
        
        return total ;
    }
}