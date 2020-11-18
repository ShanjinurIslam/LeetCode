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


    public void ReverseString(char[] s) {
        for(int i=0;i<s.Length/2;i++){
            char temp = s[i];
            s[i] =  s[s.Length-1 -i];
            s[s.Length-1 -i] = temp ;
        }
    }
}