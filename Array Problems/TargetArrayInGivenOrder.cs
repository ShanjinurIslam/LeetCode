public class Solution {
    public int[] CreateTargetArray(int[] nums, int[] index) {
        int[] target = new int[nums.Length] ;
        int max_index = -1;
        
        for(int i=0;i<nums.Length;i++){
            int prev = target[index[i]] ;
            int curr ;
            for(int j=index[i]+1;j<nums.Length;j++){
                curr = target[j];
                target[j] = prev;
                prev = curr ;
            }
            target[index[i]] = nums[i] ;
        }
        
        return target; 
    }
}