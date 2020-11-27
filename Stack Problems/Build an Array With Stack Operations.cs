public class Solution {
    public List<string> BuildArray(int[] target, int n)
        {
            List<string> operations = new List<string>();

            int index = 0;

            for(int i = 1; i <= n; i++)
            {
                if (i == target[index])
                {
                    operations.Add("Push");
                    index += 1;
                }
                else
                {
                    operations.Add("Push");
                    operations.Add("Pop");
                }
                
                if(index == target.Length)
                {
                    break;
                }
            }

            return operations;
        }
}