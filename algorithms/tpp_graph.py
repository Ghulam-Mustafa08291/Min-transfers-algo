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
        print("self.id=",id," self.u=",u," self.v=",v," self.dep=",dep," self.arr=",dep+dur," self.vid=",vid)


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

        # Sort outgoing lists by departure time (in decreasing order)
        for u, lst in start_map.items():
            lst.sort(key=lambda i: self.nodes[i].dep, reverse=True)
            start_map[u] = lst

        # Build adjacency list: for each trip, link to all valid next trips
        for x in self.nodes:
            # look at all trips that depart from x.v, in descending dep time
            for j in start_map[x.v]:
                y = self.nodes[j]

                # **Temporal validity**: only if y.dep >= x.arr
                if y.dep < x.arr:
                    # since list is sorted descending by dep, we can break here
                    break

                # weight = 0 if same vehicle, else 1
                w = 0 if x.vid == y.vid else 1

                # avoid duplicate edges
                if (y.id, w) not in self.adj[x.id]:
                    self.adj[x.id].append((y.id, w))
