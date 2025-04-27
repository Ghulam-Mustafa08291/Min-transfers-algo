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
                    # print("y is:",y)
                    q.append(y)
                    in_q[y] = True
    return dict(min_hops)

def nq_min_transfers(tpp: TPPGraph, source: int): #this processes nodes level by level without quesus
   
    INF = float('inf')
    node_min = [INF]*tpp.n
    min_hops = defaultdict(lambda: INF)
    active = [False]*tpp.n

    # Initialize
    for x in range(tpp.n):
        if tpp.nodes[x].u == source:
            node_min[x] = 0
            min_hops[tpp.nodes[x].v] = 0
            active[x] = True

    max_level = max(tpp.level)
    for _ in range(max_level+1):
        new_active = [False]*tpp.n
        for x in range(tpp.n):
            if active[x]:
                for y,w in tpp.adj[x]:
                    new_h = node_min[x] + w
                    if new_h < node_min[y]:
                        node_min[y] = new_h
                        min_hops[tpp.nodes[y].v] = min(min_hops[tpp.nodes[y].v], new_h)
                        new_active[y] = True
        active = new_active
    return dict(min_hops)

def mq_min_transfers(tpp: TPPGraph, source: int):
    """
    Multiple Queues Algorithm (MQ)
    Uses one queue per level.
    """
    INF = float('inf')
    node_min = [INF]*tpp.n
    min_hops = defaultdict(lambda: INF)

    max_level = max(tpp.level)
    level_qs = [deque() for _ in range(max_level+1)]
    in_q = [False]*tpp.n

    # Initialize
    for x in range(tpp.n):
        if tpp.nodes[x].u == source:
            node_min[x] = 0
            min_hops[tpp.nodes[x].v] = 0
            lvl = tpp.level[x]
            level_qs[lvl].append(x)
            in_q[x] = True

    # Process
    for lvl in range(max_level+1):
        q_lvl = level_qs[lvl]
        while q_lvl:
            x = q_lvl.popleft()
            in_q[x] = False
            for y,w in tpp.adj[x]:
                new_h = node_min[x] + w
                if new_h < node_min[y]:
                    node_min[y] = new_h
                    min_hops[tpp.nodes[y].v] = min(min_hops[tpp.nodes[y].v], new_h)
                    lvl_y = tpp.level[y]
                    if not in_q[y]:
                        level_qs[lvl_y].append(y)
                        in_q[y] = True
    return dict(min_hops)






















def pq_min_transfers(tpp: TPPGraph, source: int):
    print("will try to implement this")

def mpq_min_transfers(tpp: TPPGraph, source:	int):
   print("will try to implement this")




