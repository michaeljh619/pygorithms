# import base search class
from base_search import BaseSearch

# import digraph
from digraph import DirectedGraph, Vertex


class DepthFirstSearch(BaseSearch):
    @staticmethod
    def recursive_search(vertex, id_to_find, path, searched_vertices):
        # check if this is the vertex we are looking for
        if vertex.id_num == id_to_find:
            return path + [vertex.id_num]
        # check neighbors
        elif len(vertex.neighbors) > 0:
            # add this vertex to searched to prevent loops
            searched_vertices.append(vertex.id_num)
            # search neighbors that haven't already been searched
            for n in vertex.neighbors:
                if n.id_num not in searched_vertices:
                    p = DepthFirstSearch.recursive_search(
                                        n, id_to_find,
                                        path + [vertex.id_num],
                                        searched_vertices)
                    if p is not None:
                        return p
        # reaching here means all neighbors were searched and no
        # paths were found
        return None

    @staticmethod
    def search(g, starting_id, ending_id):
        # perform some post filtering
        v = super(DepthFirstSearch,
                  DepthFirstSearch).search(g, starting_id,
                                           ending_id)

        # perform recursive search
        return DepthFirstSearch.recursive_search(v, ending_id, [], [])
