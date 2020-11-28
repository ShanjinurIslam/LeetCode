/*
// Definition for a Node.
public class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
}
*/

public class Solution {
    public Node Connect(Node root)
        {
            if(root == null){
                return null;
            }
            
            Dictionary<int, List<Node>> hash_map = new Dictionary<int, List<Node>>();
            Queue<Tuple<Node, int>> queue = new Queue<Tuple<Node, int>>();

            queue.Enqueue(new Tuple<Node, int>(root, 0));

            while(queue.Count > 0)
            {
                Tuple<Node, int> u = queue.Dequeue();

                if (hash_map.ContainsKey(u.Item2)) {
                    hash_map[u.Item2].Add(u.Item1);
                }
                else
                {
                    hash_map[u.Item2] = new List<Node>();
                    hash_map[u.Item2].Add(u.Item1);
                }

                if (u.Item1.left != null)
                {
                    queue.Enqueue(new Tuple<Node, int>(u.Item1.left, u.Item2+1));
                }
                if (u.Item1.right != null)
                {
                    queue.Enqueue(new Tuple<Node, int>(u.Item1.right, u.Item2 + 1));
                }
            }

            foreach(int key in hash_map.Keys)
            {
                List<Node> arr = hash_map[key];

                for(int i = 0; i < arr.Count - 1; i++)
                {
                    arr[i].next = arr[i+1];
                }
            }
            

            return root;

        }
}