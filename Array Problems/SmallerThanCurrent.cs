public class Solution {
    public int[] SmallerNumbersThanCurrent(int[] nums) {
        int[] result = new int[nums.Length];
        
        for(int i=0;i<result.Length;i++){
            result[i] = 0 ;
            for(int j=0;j<nums.Length;j++){
                if(nums[i]>nums[j] && j!=i){
                    result[i] += 1;
                }
            }
        }
        
        return result ;
    }
}