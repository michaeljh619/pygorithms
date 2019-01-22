# import base search class
from base_search import BaseSearch

# import digraph
from digraph import DirectedGraph, Vertex

# import queue from stlib
from Queue import Queue


class BreadthFirstSearch(BaseSearch):
    @staticmethod
    def search(g, starting_id, ending_id):
        # perform some post filtering
        v = super(BreadthFirstSearch,
                  BreadthFirstSearch).search(g, starting_id,
                                             ending_id)
        # create a queue
        q = Queue()

        # add starting vertex to queue and start to search
        checked_vertex_ids = []
        q.put((v, []))
        # each item in queue is the vertex with its path
        while not q.empty():
            # dequeue vertex and path
            v, path = q.get()
            # check if this vertex is the one we are searching for
            if v.id_num == ending_id:
                return path
            # else check if already visited
            elif v.id_num in checked_vertex_ids:
                pass
            # else this is a new vertex we are visiting
            else:
                # add to checked vertices
                checked_vertex_ids.append(v.id_num)
                # check neighbors
                for n in v.neighbors:
                    n_path = path + [n.id_num]
                    q.put((n, n_path))

        # no path was found
        return None
