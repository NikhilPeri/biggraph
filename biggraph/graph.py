import pandas as pd
import dask.dataframe as dd

class DictGraph(object):
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        try:
            self.nodes[node]
        except KeyError:
            self.nodes[node] = {}

    def add_edge(self, node_1, node_2, weight):
        try:
            self.nodes[node_1][node_2] = weight
        except:
            self.nodes[node_2] = {node_2 : weight}

    def get_edge(self, node_1, node_2):
        try:
            return self.nodes[node_1][node_2]
        except:
            return None

class DaskGraph(object):
    def __init__(self):
        self.nodes = dd.from_pandas(
            pd.DataFrame(columns=['node_1', 'node_2', 'weight']).set_index(['node_1'], drop=False),
            chunksize=1e9
        )

    def add_edge(self, node_1, node_2, weight):
        import pdb; pdb.set_trace()
