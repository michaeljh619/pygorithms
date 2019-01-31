# import base search class
from base_search import BaseSearch

# import digraph
from digraph import DirectedGraph, Vertex

# import queue from stlib
import heapq


class Dijkstra(BaseSearch):
    @staticmethod
    def search(g, starting_id, ending_id):
        # perform some post filtering
        v = super(Dijkstra,
                  Dijkstra).search(g, starting_id, ending_id)

        # create a priority queue
        # 1st tuple elem: weight of path to this vertex (cmp)
        # 2nd tuple elem: the vertex
        # 3rd tupl elem: the path of id's to this vertex
        pq = [(0, v, [starting_id])]

        # add starting vertex to queue and start to search
        checked_vertex_ids = []
        heapq.heapify(pq)

        # loop through q getting highest priority each time
        while len(pq) > 0:
            # dequeue vertex and path
            weight, v, path = heapq.heappop(pq)
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
                    n_weight = weight + v.get_weight(n.id_num)
                    heapq.heappush(pq, (n_weight, n, n_path))

        # no path was found
        return None
