public class Solution {
    public string GetMonth(string month)
        {
            Dictionary<string, string> map = new Dictionary<string, string>();
            map["Jan"] = "01";
            map["Feb"] = "02";
            map["Mar"] = "03";
            map["Apr"] = "04";
            map["May"] = "05";
            map["Jun"] = "06";
            map["Jul"] = "07";
            map["Aug"] = "08";
            map["Sep"] = "09";
            map["Oct"] = "10";
            map["Nov"] = "11";
            map["Dec"] = "12";
            return map[month];
        }

        public string GetDay(string val)
        {
            val = val.Remove(val.Length - 2, 2);
            if(val.Length == 1)
            {
                val = "0" + val;
                return val;
            }
            else
            {
                return val;
            }
        }
    
    public string ReformatDate(string date)
        {
            string[] arr = date.Split(' ');
            return arr[2] +"-" +  this.GetMonth(arr[1]) + "-" + this.GetDay(arr[0]);
        }
}