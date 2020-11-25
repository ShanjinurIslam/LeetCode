class Solution(object):
    def find_all(self,string,char):
        indexes = []
        
        for i,each in enumerate(string):
            if each == char:
                indexes.append(i)
                
        return indexes
    
    def subdomainVisits(self, cpdomains):
        hash_map = {}
        
        for each in cpdomains:
            arr = [str(x) for x in each.split()]
            count = int(arr[0])
            
            indexes = self.find_all(arr[1],".")
            
            if arr[1] in hash_map:
                hash_map[arr[1]] += count
            else:
                hash_map[arr[1]] = count
                
            for each in indexes:
                domain = arr[1][each+1:]
                if domain in hash_map:
                    hash_map[domain] += count
                else:
                    hash_map[domain] = count
                    
        final = []
        
        for each in hash_map.keys():
            final.append(str(hash_map[each])+" "+each)
        
        return final
        
        
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        