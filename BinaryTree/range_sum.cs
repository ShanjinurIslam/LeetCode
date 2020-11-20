public class Solution {
    private int sum = 0 ;
    
    private void SumFunction(TreeNode root,int low,int high){
        if(root==null){
            return;
        }
        else{
            if(root.val>=low && root.val<=high){
                this.sum += root.val ;
            }
            
            this.SumFunction(root.left,low,high);
            this.SumFunction(root.right,low,high);
        }
    }
    
    public int RangeSumBST(TreeNode root, int low, int high) {
        this.sum = 0 ;
        this.SumFunction(root,low,high);
        return this.sum;
    }
}