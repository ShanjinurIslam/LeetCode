public class Solution {
    public int MaxNumberOfBalloons(string text)
        {
            Dictionary<char, int> pairs = new Dictionary<char, int>();

            char[] keys = { 'b', 'a', 'l','o', 'n' };

            for (int i = 0; i < keys.Length; i++) {
                pairs[keys[i]] = 0;
            }

            for(int i = 0; i < text.Length; i++)
            {
                if (pairs.ContainsKey(text[i]))
                {
                    pairs[text[i]] += 1;
                }
            }

            pairs['l'] /= 2;
            pairs['o'] /= 2;

            int min = text.Length;

            for(int i = 0; i < keys.Length; i++)
            {
                min = Math.Min(pairs[keys[i]], min);
            }

            return min;
        }

}