class Vertex:
    # neighbors is a list of tuples where:
    # element 1 in the tuple is a node
    # element 2 in the tuple is the weight or distance

    def __init__(self, id_num_in):
        self.id_num = id_num_in
        self.neighbors = []
        self.weights = []

    def connect(self, vertex, weight):
        self.neighbors.append(vertex)
        self.weights.append(weight)

    def get_neighbor(self, id_num):
        return next((v for v in self.neighbors if v.id_num == id_num),
                    None)

    def get_weight(self, id_num):
        for i in range(len(self.neighbors)):
            if self.neighbors[i].id_num == id_num:
                return self.weights[i]
        # else neighbor does not exist
        return None


class DirectedGraph:

    def __init__(self, adjacency_list):
        self.vertices = []

        for a in adjacency_list:
            # get id's
            id_0 = a[0]
            id_1 = a[1]

            # if adjacency list does not have weights, use 1
            weight = 1
            if len(a) == 3:
                weight = a[2]

            # get vertex with id_0 if in list, else create new one
            v0 = next((v for v in self.vertices if v.id_num == id_0),
                      None)
            if not v0:
                v0 = Vertex(id_0)
                self.vertices.append(v0)

            # do the same with id_1
            v1 = next((v for v in self.vertices if v.id_num == id_1),
                      None)
            if not v1:
                v1 = Vertex(id_1)
                self.vertices.append(v1)

            # connect the two
            v0.connect(v1, weight)

    def get_vertex(self, id_num):
        return next((v for v in self.vertices if v.id_num == id_num),
                    None)
