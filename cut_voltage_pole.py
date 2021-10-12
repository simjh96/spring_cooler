def solution(n, wires):
    class Node:
        def __init__(self, key):
            self.key = key

            # append only key of obj
            self.connections = []
            self.child = []
            self.parent = []
            self.cum = 0

    class Graph:
        def __init__(self, n):
            self.nodes = []
            for _ in range(n):
                self.nodes.append(Node(_))

        def set_link(self, link):
            self.nodes[link[0] - 1].connections.append(link[1] - 1)
            self.nodes[link[1] - 1].connections.append(link[0] - 1)

        def sort_parent(self, current_key, parent_key=None) -> 'void':
            if parent_key is None:
                # root
                print(f'node {current_key} is root')
                self.nodes[current_key].child = self.nodes[current_key].connections
                for child_key in self.nodes[current_key].child:
                    self.nodes[child_key].parent = current_key
                    self.sort_parent(child_key, current_key)

            else:
                current_node = self.nodes[current_key]
                self.nodes[current_key].child = [node_key for node_key in current_node.connections if
                                                 node_key != parent_key]
                print(f'node {current_key} : len(self.nodes[current_key].child) : {len(self.nodes[current_key].child)}')
                if len(self.nodes[current_key].child):
                    for child_key in self.nodes[current_key].child:
                        self.nodes[child_key].parent = current_key
                        self.sort_parent(child_key, current_key)

        def cum_child_cnt(self, current_key, parent_key=None) -> 'cum_child':
            if parent_key is None:
                # root
                print(f'node {current_key} is root')

                for child_key in self.nodes[current_key].child:
                    self.nodes[current_key].cum += self.cum_child_cnt(child_key, current_key)
                    return self.nodes[current_key].cum
            else:
                if len(self.nodes[current_key].child):
                    for child_key in self.nodes[current_key].child:
                        increment = self.cum_child_cnt(child_key, current_key)
                        self.nodes[current_key].cum += increment
                        print(f"node:{current_key} 's cum was added +{increment} by child {child_key}")
                    self.nodes[current_key].cum += 1
                    return self.nodes[current_key].cum
                else:
                    self.nodes[current_key].cum = 1
                    return self.nodes[current_key].cum

    G = Graph(n)
    for w in wires:
        G.set_link(w)
    print('*************************')
    for n_ in G.nodes:
        print(f'node {n_.key}: connected to {n_.connections}')

    print('*************************')

    for node in G.nodes:
        if len(node.connections) == 1:
            break

    print(node.key)

    G.sort_parent(node.key)
    G.cum_child_cnt(node.key)

    for n_ in G.nodes:
        print('====================')
        print(f'node {n_.key} : {n_.cum} cum nodes')
        print(f'parent : {n_.parent}')
        print(f'child : {n_.child}')

    sep_node = min(range(n), key=lambda x: abs(n / 2 - G.nodes[x].cum))
    sep_cum = G.nodes[sep_node].cum

    return abs(n - 2 * sep_cum)

