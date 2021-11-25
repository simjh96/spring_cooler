# g
class Node:
    def __init__(self):
        self.edge = set()


class Graph:
    def __init__(self, r, c, conn, q):
        self.r = r
        self.c = c
        self.conn = conn
        self.q = q
        self.nodes = dict()
        for _r in range(1, r+1):
            for _c in range(1, c+1):
                self.nodes[(_r, _c)] = Node()
        self.set_conn()
        print(self.nodes[(1, 2)].edge)
        self.answer = self.cpt_queries()

    def set_conn(self):
        for c in self.conn:
            r1, c1, r2, c2 = c
            self.nodes[(r1, c1)].edge.add((r2 - r1, c2 - c1))
            self.nodes[(r2, c2)].edge.add((r1 - r2, c1 - c2))

    def cpt_queries(self):
        result = []
        for _q in self.q:
            result.append(self.cpt_query(_q))
            print("======================")
        return result

    def cpt_query(self, query):
        cnt = 0
        r1, c1, r2, c2 = query
        max_r, max_c = max([r1, r2]), max([c1, c2])
        min_r, min_c = min([r1, r2]), min([c1, c2])

        cnt += self.cnt_link((min_r, min_c), [(-1,0), (0,-1)])
        cnt += self.cnt_link((min_r, max_c), [(-1,0), (0,1)])
        cnt += self.cnt_link((max_r, max_c), [(1,0), (0,1)])
        cnt += self.cnt_link((max_r, min_c), [(1,0), (0,-1)])
        for _r in range(min_r+1, max_r):
            print(f'_r, c : {_r, min_c} , {_r, max_c}')
            cnt += self.cnt_link((_r, min_c), [(0,-1)])
            cnt += self.cnt_link((_r, max_c), [(0,1)])
        for _c in range(min_c+1, max_c):
            print(f'_c : {_c}')
            cnt += self.cnt_link((min_r, _c), [(-1,0)])
            cnt += self.cnt_link((max_r, _c), [(1,0)])
        return cnt

    def cnt_link(self, _key, drts):
        cnt = 0
        for d in drts:
            if d in self.nodes[_key].edge:
                cnt += 1
                self.nodes[_key].edge.remove(d)
                self.nodes[(_key[0]+d[0], _key[1]+d[1])].edge.remove((-d[0], -d[1]))
                print(f'removed link : {_key} <-> {(_key[0]+d[0], _key[1]+d[1])}')
        return cnt


rows, columns, connections, queries = 4, 3, [[1, 1, 2, 1], [1, 2, 1, 3], [1, 3, 2, 3], [2, 2, 2, 3], [2, 2, 3, 2],
                                             [2, 3, 3, 3], [3, 2, 3, 3], [3, 2, 4, 2], [4, 1, 4, 2]], [[2, 2, 3, 1],
                                                                                                       [1, 2, 4, 2]]
G = Graph(rows, columns, connections, queries)
print(G.answer)
print(G.nodes[(1,2)].edge)



