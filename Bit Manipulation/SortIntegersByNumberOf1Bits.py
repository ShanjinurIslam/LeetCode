class Solution(object):
    def sortByBits(self, arr):
        return [x[1] for x in sorted([(bin(arr[i]).count("1"),arr[i]) for i in range(len(arr))])]