public class Solution {
    public int NumberOfSteps (int num) {
        int number_of_steps = 0 ;
        
        while(num>0){
            if(num%2==0){
                num = num/2 ;
                number_of_steps += 1 ;
            }
            else{
                num -= num%2 ;
                number_of_steps += 1 ;
            }
        }
        
        return number_of_steps;
    }
}