import sparse
import dask.array as da

class Graph(object):

    def __init__(self):
        self.nodes = da.array([])
        self.edges = da.array([[]])

    def edge(self, node_a, node_b):
        return self.
