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

