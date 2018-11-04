# Disjointed-Set Union
class DSU(object):
    def __init__(self):
        self.parents = range(1001)
        self.ranks = [0] * 1001

    def query(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.query(self.parents[x])
        return self.parents[x]

    def connect(self, x, y):
        xr, yr = self.query(x), self.query(y)
        if xr == yr:
            return False
        elif self.ranks[xr] < self.ranks[yr]:
            self.parents[xr] = yr
        elif self.ranks[xr] > self.ranks[yr]:
            self.parents[yr] = xr
        else:
            self.parents[yr] = xr
            self.ranks[xr] += 1
        return True