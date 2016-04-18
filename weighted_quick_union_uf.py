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


