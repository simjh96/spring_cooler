import sys
sys.setrecursionlimit(10**6)


class Graph:
    def __init__(self, n_len):
        # adjacent matrix
        self.visited = set()
        self.n_len = n_len
        self.adj_matrix = dict()
        for _ in range(self.n_len):
            self.adj_matrix[_] = set()

        # super node
        self.super_node = self.n_len
        self.adj_matrix[self.super_node] = set()
        for _1 in range(self.n_len):
            self.add_edge((self.super_node, _1))

        # result
        self.flag = 0

    def add_edge(self, edge):
        self.adj_matrix[edge[0]].add(edge[1])
        self.adj_matrix[edge[1]].add(edge[0])


def brute_force(graph_, start, path=None) -> 'void':
    if path is None:
        path = [start]
    print('  ' * len(path) + f'start : {start}')
    print('  ' * len(path) + f'graph_.adj_matrix[start] : {graph_.adj_matrix[start]}')

    if len(path) < 6:
        for end in graph_.adj_matrix[start]:
            print('  ' * len(path) + '  ====================================================')
            print('  ' * len(path) + f'  start : {start}')
            print('  ' * len(path) + f'  end : {end}')
            if (end not in path) and (graph_.flag == 0):
                print('  ' * len(path) + f'  calling brute_force')
                print('  '*len(path) + f'  current path : {path}')
                print('  '*len(path) + f'  appending edge {start} -> {end}')
                brute_force(graph_, end, path + [end])


    else:
        graph_.flag = 1
        print(f'final path : {path}')


n, m = list(map(int, sys.stdin.readline().strip().split()))
g = Graph(n)

for _ in range(m):
    g.add_edge(list(map(int, sys.stdin.readline().strip().split())))

brute_force(g, g.super_node)
print(g.flag)
