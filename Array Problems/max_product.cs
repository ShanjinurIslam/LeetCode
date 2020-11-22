public class Solution {
    public int MaxProduct(int[] nums) {
        Array.Sort<int>(nums);
        Array.Reverse(nums);
        return (nums[0]-1)*(nums[1]-1);
    }
}