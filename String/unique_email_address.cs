using System;
using System.Collections.Generic;


public class Solution {
    public int NumUniqueEmails(string[] emails)
        {
            Dictionary<string, bool> mails = new Dictionary<string, bool>();

            for (int i = 0; i < emails.Length; i++)
            {
                string[] arr = emails[i].Split('@');

                arr[0] = arr[0].Replace(".", "");

                int length = arr[0].IndexOf('+');
                if (length != -1)
                {
                    arr[0] = arr[0].Substring(0, length);
                }

                if (!mails.ContainsKey(arr[0]+arr[1]))
                {
                    mails[arr[0]+"@"+arr[1]] = true;
                }
            }

            return mails.Count;
        }
}