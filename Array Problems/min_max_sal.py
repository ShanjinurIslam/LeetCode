class Solution(object):
    def average(self, salary):
        min_sal = min(salary)
        max_sal = max(salary)
        
        return ((sum(salary)-min_sal-max_sal)*1.0)/(len(salary) - 2)
        
        """
        :type salary: List[int]
        :rtype: float
        """
        