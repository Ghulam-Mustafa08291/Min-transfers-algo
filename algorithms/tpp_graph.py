from collections import defaultdict, deque


class TemporalEdge:
    """
    Represents an edge (trip) in the temporal graph.
    id: unique identifier for the edge
    u: start vertex
    v: end vertex
    dep: departure time
    arr: arrival time
    vid: vehicle ID
    """
    def __init__(self, id, u, v, dep, dur, vid):
        self.id = id
        self.u = u
        self.v = v
        self.dep = dep
        self.arr = dep + dur
        self.vid = vid


class TPPGraph:
    """
    Temporal Paths Preservation (TPP) Graph:
    - Transforms a temporal graph (list of trips) into a DAG where each trip is a node.
    - Adds edges between trips that are time-respecting (arrival <= next departure).
    - Edge weight = 0 if same vehicle, else 1.
    - Computes a 'level' for each node via topological ordering.
    """
    def __init__(self, trips):
        # trips: list of tuples (u, v, dep, dur, vid)
        self.nodes = [TemporalEdge(i, u, v, dep, dur, vid)
                      for i,(u,v,dep,dur,vid) in enumerate(trips)]
        self.n = len(self.nodes)
        self.adj = [[] for _ in range(self.n)]
        self.level = [0]*self.n
        self._build()

    def _build(self):
        # Group trips by their start station for adjacency construction
        start_map = defaultdict(list)
        for node in self.nodes:
            start_map[node.u].append(node.id)
        # Sort outgoing lists by departure time descending
        for u, lst in start_map.items():
            lst.sort(key=lambda i: self.nodes[i].dep, reverse=True)
            start_map[u] = lst
        # Build adjacency: for each trip, link to all valid next trips
        for x in self.nodes:
            for j in start_map[x.v]:
                y = self.nodes[j]
                if y.dep >= x.arr:
                    w = 0 if x.vid == y.vid else 1
                    self.adj[x.id].append((y.id, w))
                else:
                    break
        # Compute levels via topological sort (DAG)
        indeg = [0]*self.n
        for u in range(self.n):
            for v,_ in self.adj[u]:
                indeg[v] += 1
        q = deque([i for i in range(self.n) if indeg[i]==0])
        while q:
            u = q.popleft()
            for v,_ in self.adj[u]:
                self.level[v] = max(self.level[v], self.level[u] + 1)
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        print("in TPP graph class,final djacency List:", self.adj)  
