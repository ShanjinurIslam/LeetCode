public class Solution {
    public  string RestoreString(string s, int[] indices)
    {
            string new_string = s;
            char[] arr = new_string.ToCharArray();

            for (int i = 0; i < s.Length; i++)
            {
                arr[indices[i]] = s[i];
            }

            return new String(arr);
    }
}