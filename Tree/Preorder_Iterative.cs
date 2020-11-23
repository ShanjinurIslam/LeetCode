// list version
public class Solution {
    public List<int> Preorder(Node root) {
        List<int> arr = new List<int>();
        List<Node> nodes = new List<Node>();
        nodes.Add(root);
        
        while(nodes.Count>0){
            Node node = nodes[0];
            nodes.RemoveAt(0);
            
            if(node == null){
                continue;
            }
            
            arr.Add(node.val);
            
            for(int i=0;i<node.children.Count;i++){
                nodes.Insert(i,node.children[i]);
            }
        }
        
        //arr.Reverse();
        return arr;
    }
}

// stack version
public class Solution {
    public List<int> Preorder(Node root) {
        List<int> arr = new List<int>();
        Stack<Node> nodes = new Stack<Node>();
        nodes.Push(root);
        
        while(nodes.Count>0){
            Node node = nodes.Pop();
            
            if(node == null){
                continue;
            }
            
            arr.Add(node.val);
            
            for(int i=node.children.Count-1;i>=0;i--){
                nodes.Push(node.children[i]);
            }
        }
        
        //arr.Reverse();
        return arr;
    }
}