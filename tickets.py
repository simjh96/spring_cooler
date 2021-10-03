def solution(tickets):
    g = Graph()
    for t in tickets:
        g.input_link(*t)

    result = g.solution()

    return result


class Node:
    def __init__(self, key):
        self.key = key

        # append as Node object
        self.out = []
        self.inner = []
        # in - out
        self.diff = 0

    def push(self, dirc, new: 'Node'):
        if dirc == 'out':
            self.out.append(new)
            self.diff -= 1
        else:
            self.inner.append(new)
            self.diff += 1

    def sort(self):
        self.out.sort(key=lambda x: x.key)


class Graph:
    def __init__(self):
        self.nodes = dict()

        self.start = 'ICN'
        self.visited = set()

    def input_link(self, _from, _to):
        # if new
        if _from not in self.nodes:
            self.nodes[_from] = Node(_from)
        if _to not in self.nodes:
            self.nodes[_to] = Node(_to)

        self.nodes[_from].push('out', self.nodes[_to])
        self.nodes[_to].push('in', self.nodes[_from])

    def sort_all(self):
        [self.nodes[key].sort() for key in self.nodes]

    def _find_end(self):
        for node_key in self.nodes:
            if self.nodes[node_key].diff == 1:
                self.end = node_key

    def find_back_bone(self):
        self._find_end()

        self.sort_all()

        # dfs
        # find latest(in alphbet order) path ending with 'self.end'
        self.visited.add('ICN')

        paths = ['ICN']

        self.back_bone = self.dfs(paths)

        return self.back_bone

    def dfs(self, paths) -> 'paths':
        # single step
        i = len(paths)
        last_node = paths[-1]

        # from largest alph order
        for node in self.nodes[last_node].out[::-1]:
            if node.key == self.end:
                return paths + [node.key]
            else:
                if node.key not in self.visited:
                    self.visited.add(node.key)
                    paths_ = self.dfs(paths + [node.key])

                    # return 받는 일이 생기면 바로 function end
                    if paths_:
                        return paths_

    def solution(self):
        result = []
        self.find_back_bone()

        # pop all exit back bone root
        for _ in range(len(self.back_bone)):
            if _ + 1 < len(self.back_bone):
                out = self.nodes[self.back_bone[_]].out
                for _1 in range(len(out)):
                    if out[_1].key == self.back_bone[_ + 1]:
                        out.pop(_1)
                        break

        # for each bone
        for _2 in self.back_bone:
            result.append(_2)

            # travel through all residual, in alpha low order
            current = self.nodes[_2]
            while current.out:
                next_key = current.out[0].key
                result.append(next_key)
                current.out.pop(0)

                current = self.nodes[next_key]

        return result


# 시작 : 시작이 끝보다 하나 더 많음
# 중간 : 시작과 끝이 빈도가 같음
# 끝: 시작보다 끝이 하나 더 많음

# count로 하나 조지고 O(n)

# 토대로 연결 O()


tickets = [["ICN", "JFK"], ["JFK", "ICN"], ["ICN", "JFK"]]
print(solution(tickets))