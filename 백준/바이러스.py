"""
Union Find로 풀었지만
실패(런타임 에러)
"""

import sys

input = sys.stdin.readline


class UnionFinds:
    def __init__(self, n: int):
        self.nodes = n
        self.parents = [i for i in range(n + 1)]

    def find(self, node):
        if node != self.parents[node]:
            self.find(self.parents[node])
        return self.parents[node]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        as_is, to_be = -1, -1
        if x_parent == y_parent:
            return
        elif x_parent < y_parent:
            as_is, to_be = y_parent, x_parent
        elif x_parent > y_parent:
            as_is, to_be = x_parent, y_parent

        for i in range(n):
            if self.parents[i] == as_is:
                self.parents[i] = to_be

    def has_nodes(self, node):
        return len(list(filter(lambda x: x == node, self.parents)))


if __name__ == '__main__':
    computers = int(input())
    n = int(input())
    viruses = UnionFinds(computers)
    for _ in range(n):
        a, b = map(int, input().split())
        viruses.union(a, b)
    print(viruses.has_nodes(1))
