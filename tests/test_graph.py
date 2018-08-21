import pytest

from biggraph import Graph

@pytest.fixture
def empty_graph():
    return Graph()

class TestGraph(object):
    def test_init_creates_new_empty_graph(self, empty_graph):
        assert empty_graph.nodes.count() == 0

    def test_add_node_creates_new_node(self):
        graph.add_node('a')
        assert sorted(graph.nodes) == sorted(['a'])

    def test_add_edge_creates_new_node_if_missing(self):
        graph.add_node('a')
        graph.add_edge('a', 'b', 1.0)
        assert sorted(graph.nodes) == sorted(['a', 'b'])

    def test_add_edge_creates_
