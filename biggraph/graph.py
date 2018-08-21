import sparse
import dask.array as da

class Graph(object):

    def __init__(self, max_partition_size=1e4, nodes=da.array([]), edges=da.array([[]])):
        self.nodes = nodes
        self.edges = edges
