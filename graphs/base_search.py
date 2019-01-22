class BaseSearch(object):
    @staticmethod
    def search(graph_to_search, starting_vertex_id, ending_vertex_id):
        # return starting vertex
        return graph_to_search.get_vertex(starting_vertex_id)
