/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int MaxLevelSum(TreeNode root)
        {
            if (root == null)
            {
                return 0;
            }

            Dictionary<int,int> level_wise_data = new Dictionary<int,int>();

            Queue<Tuple<TreeNode, int>> queue = new Queue<Tuple<TreeNode, int>>();

            queue.Enqueue(new Tuple<TreeNode, int>(root, 0));

            while (queue.Count > 0)
            {
                Tuple<TreeNode, int> s = queue.Dequeue();

                if (level_wise_data.ContainsKey(s.Item2))
                {
                    level_wise_data[s.Item2] += s.Item1.val;
                }
                else
                {
                    level_wise_data[s.Item2] = s.Item1.val;
                }

                if (s.Item1.left != null)
                {
                    queue.Enqueue(new Tuple<TreeNode, int>(s.Item1.left, s.Item2+1));
                }

                if (s.Item1.right != null)
                {
                    queue.Enqueue(new Tuple<TreeNode, int>(s.Item1.right, s.Item2 + 1));
                }
            }

            int max_val = int.MinValue;
            int level = -1;    
        
            foreach(int key in level_wise_data.Keys)
            {
                if(max_val<level_wise_data[key]){
                    level = key;
                    max_val = level_wise_data[key];
                }
            }

            return level+1;
        }
}