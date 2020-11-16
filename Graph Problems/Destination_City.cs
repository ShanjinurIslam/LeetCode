public class Solution {
    public string DestCity(IList<IList<string>> paths) {
        Dictionary<String,int> in_degree = new Dictionary<String,int>();
        Dictionary<String,int> out_degree = new Dictionary<String,int>();
        
        foreach(IList<string> path in paths){
            if(in_degree.ContainsKey(path[1])){
                in_degree[path[1]] += 1;
            }
            else{
                in_degree[path[1]] = 1;
                out_degree[path[1]] = 0;
            }
            if(out_degree.ContainsKey(path[0])){
                out_degree[path[0]] += 1;
            }
            else{
                out_degree[path[0]] = 1;
                in_degree[path[0]] = 0;
            }
        }
        
        string final_city = "";
               
        foreach(string key in out_degree.Keys){
            if(out_degree[key]==0){
                final_city = key ;
                break ;
            }
        }
        
        return final_city ;
        
    }
}