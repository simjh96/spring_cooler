import sys


class Node:

    def __init__(self, val):
        self.val = val
        self.connections = set()
        self.parent = None
        self.child = set()


class Tree:

    def __init__(self, len_n: '[1: n+1]'):
        self.len = len_n
        # leave [0] as blank
        self.listed = [Node(i) for i in range(len_n + 1)]

    def link(self, connection: list):
        self.listed[connection[0]].connections.add(connection[1])
        self.listed[connection[1]].connections.add(connection[0])
        print('current connection : ', [_node.connections for _node in self.listed])

    def sort(self, target: int = 1, parent: int = None, debug = 0) -> 'void':
        debug += 1
        # set root
        print('  ' * debug + 'current parent : ', [_node.parent for _node in self.listed])
        print('  '*debug + f'sort(target:{target},parent:{parent})')

        if target == 1:
            self.listed[1].child = self.listed[1].connections
            [self.sort(child, 1, debug) for child in self.listed[1].child]

        if len(self.listed[target].connections) == 1:
            self.listed[target].parent = parent
            print('  ' * debug + f'===================End of Tree===================')
            return

        # recurse sort
        else:
            self.listed[target].parent = parent
            self.listed[target].child = self.listed[target].connections - {parent}
            [self.sort(child, target, debug) for child in self.listed[target].child]


n = int(sys.stdin.readline().strip())
my_tree = Tree(n)

# input all connections
for _ in range(n - 1):
    my_tree.link(list(map(int, sys.stdin.readline().strip().split())))

# sort
my_tree.sort()

for i in range(2, n+1):
    print(my_tree.listed[i].parent)

