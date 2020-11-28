public class Solution
{
    public string ThousandSeparator(int n)
    {
        string s = n.ToString();
        int a = s.Length;

        for (int i = (a - 3); i > 0; i -= 3)
        {
            s = s.Insert(i, ".");
        }

        return s;

    }
}