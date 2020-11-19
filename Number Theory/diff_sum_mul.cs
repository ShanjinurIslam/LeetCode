using System.Collections.Generic;

public class Solution {
    public int SubtractProductAndSum(int n) {
        List<int> digits = new List<int>() ;
        
        while(n>0){
            digits.Add(n%10) ;
            n /= 10 ;
        }
        
        int sum = 0;
        int mul = 1;
        
        for(int i=0;i<digits.Count;i++){
            sum += digits[i] ;
            mul *= digits[i] ;
        }
        
        return mul - sum ;
    }
}