public class Solution {
    public bool isSubstring(string target,string s)
        {
            if (target.Length < s.Length)
            {
                return false;
            }
            else
            {
                for(int i = 0; i < target.Length - s.Length + 1; i++)
                {
                    if (target.Substring(i, s.Length).Equals(s))
                    {
                        return true;
                    }
                }
            }

            return false;
        }
    
    public List<string> StringMatching(string[] words) {
        List<string> final = new List<string>();
        
        for(int i=0;i<words.Length;i++){
            bool flag = false; 
            for(int j=0;j<words.Length;j++){
                if(i!=j){
                    flag |= this.isSubstring(words[j],words[i]);
                }
            }
            if(flag == true){
                final.Add(words[i]);
            }
        }
        
        return final;
    }
}