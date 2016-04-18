# coding: utf-8


class WeightedQuickUnionUF(object):

    def __init__(self, n):
        self.__count = n
        self.parent = range(n)
        self.size = [1] * n

    def find(self, p):
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def union(self, p, q):
        root_p = self.parent[p]
        root_q = self.parent[q]

        if root_p == root_q:
            return
        elif self.size[root_p] > self.size[root_q]:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        else:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        self.__count -= 1

    def count(self):
        return self.__count

    def connected(self, p, q):
        return self.find(p) == self.find(q)


if __name__ == '__main__':
    UF = WeightedQuickUnionUF(24)

    for i in xrange(23):
        UF.union(i, i+1)
    assert UF.count() == 1

    UF = WeightedQuickUnionUF(33)

    UF.union(0, 1)
    UF.union(0, 20)
    assert UF.connected(1, 20) is True

    UF.union(4, 12)
    UF.union(4, 31)
    assert UF.connected(12, 31) is True

    UF.union(0, 12)
    assert UF.connected(4, 1) is True
