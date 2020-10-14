# O(n2) solution, hugely inefficient

class Solution(object):
    def maxArea(self, height):
        max_water = 0

        n = len(height)

        for i in range(0, n-1):
            for j in range(i+1, n):
                curr_max = min(height[i], height[j])*(abs(i-j))

                if curr_max > max_water:
                    max_water = curr_max

        return max_water


# O(n) solution

class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water
