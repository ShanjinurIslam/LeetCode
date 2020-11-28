public IList<IList<int>> LevelOrder(Node root)
        {
            IList<IList<int>> traversal = new List<IList<int>>();

            if (root == null)
            {
                return traversal;
            }

            Dictionary<int, IList<int>> level_wise_nodes = new Dictionary<int, IList<int>>();
            Queue<Tuple<Node, int>> queue = new Queue<Tuple<Node, int>>();

            queue.Enqueue(new Tuple<Node, int>(root, 0));

            while (queue.Count > 0)
            {
                Tuple<Node, int> s = queue.Dequeue();

                if (level_wise_nodes.ContainsKey(s.Item2))
                {
                    level_wise_nodes[s.Item2].Add(s.Item1.val);
                }
                else
                {
                    level_wise_nodes[s.Item2] = new List<int>();
                    level_wise_nodes[s.Item2].Add(s.Item1.val);
                }

                foreach(Node child in s.Item1.children)
                {
                    if (child != null)
                    {
                        queue.Enqueue(new Tuple<Node, int>(child, s.Item2+1));
                    }
                }
            }

            foreach(int key in level_wise_nodes.Keys)
            {
                traversal.Add(level_wise_nodes[key]);
            }

            return traversal;
        }