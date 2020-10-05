import datetime


class Solution(object):
    def __init__(self):
        self.value_map = [0]*250505

    def generate_power(self, x) -> int:
        x = int(x)

        if x == 1:
            return 0
        else:
            if self.value_map[x] != 0:
                return self.value_map[x]

            if x % 2 == 0:
                self.value_map[x] = 1 + self.generate_power(x/2)
            else:
                self.value_map[x] = 1 + self.generate_power(x*3 + 1)

            return self.value_map[x]

    def getKth(self, lo, hi, k):
        value_pair = []
        for i in range(lo, hi+1):
            value_pair.append((i, self.generate_power(i)))

        value_pair.sort(key=lambda x: x[1])

        return value_pair[k-1][0]


print(Solution().getKth(1, 1, 1))
