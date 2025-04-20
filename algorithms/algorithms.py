from collections import deque, defaultdict
import heapq
from .tpp_graph import TPPGraph



def sq_min_transfers(tpp: TPPGraph, source: int):

    INF = float('inf')
    node_min = [INF]*tpp.n
    min_hops = defaultdict(lambda: INF)
    q = deque()
    in_q = [False]*tpp.n

    # Initialize source trips (edges) as nodes
    for x in range(tpp.n):
        if tpp.nodes[x].u == source:
            node_min[x] = 0
            min_hops[tpp.nodes[x].v] = 0
            q.append(x)
            in_q[x] = True

    while q:
        x = q.popleft()
        in_q[x] = False
        for y,w in tpp.adj[x]:
            new_h = node_min[x] + w
            if new_h < node_min[y]:
                node_min[y] = new_h
                min_hops[tpp.nodes[y].v] = min(min_hops[tpp.nodes[y].v], new_h)
                if not in_q[y]:
                    print("y is:",y)
                    q.append(y)
                    in_q[y] = True
    return dict(min_hops)

