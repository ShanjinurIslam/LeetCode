public class Solution {
    public List<int> Postorder(Node root) {
        List<int> arr = new List<int>();
        Stack<Node> stack = new Stack<Node>();
        stack.Push(root);
        
        while(stack.Count>0){
            Node node = stack.Pop();
            
            if(node == null){
                continue;
            }
            
            arr.Add(node.val);
            
            for(int i=0;i<node.children.Count;i++){
                stack.Push(node.children[i]);
            }
        }
        
        arr.Reverse();
        return arr;
    }
}