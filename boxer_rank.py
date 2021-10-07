def solution(n, results):
    G = Graph(n)

    # insert link
    for r in results:
        G.insert_link(r)

    # for all vertaxes, fill left_group/ right_group
    G.construct_group('left')
    G.construct_group('right')

    # count how many nodes have n-1 total group
    answer = 0
    for _ in G.nodes:
        if len(G.nodes[_].left_group) + len(G.nodes[_].right_group) == n - 1:
            answer += 1
    return answer


# graph
class Node:
    def __init__(self, key):
        self.key = key
        self.left = set()
        self.right = set()
        self.left_group = None
        self.right_group = None


class Graph:
    def __init__(self, V: int):
        self.nodes = dict()
        for _ in range(V):
            self.nodes[_ + 1] = Node(_ + 1)

    def insert_link(self, link: '[0 < 1]'):
        self.nodes[link[0]].right.add(self.nodes[link[1]])
        self.nodes[link[1]].left.add(self.nodes[link[0]])

    def construct_group(self, direction) -> 'void':
        for node_key in self.nodes:
            self._construct_group(direction, self.nodes[node_key])

    def _construct_group(self, direction, start: Node) -> 'void':
        if direction == 'left':
            if start.left_group is None:
                if len(start.left) == 0:
                    start.left_group = set()
                else:
                    for left_node in start.left:
                        if left_node.left_group is None:
                            self._construct_group(direction, left_node)

                    start.left_group = set()
                    for left_node in start.left:
                        start.left_group |= left_node.left_group | {left_node}

        if direction == 'right':
            if start.right_group is None:
                if len(start.right) == 0:
                    start.right_group = set()
                else:
                    for right_node in start.right:
                        if right_node.right_group is None:
                            self._construct_group(direction, right_node)

                    start.right_group = set()
                    for right_node in start.right:
                        start.right_group |= right_node.right_group | {right_node}


a = Node(1)
b = Node(1)
print(set([a, b]))