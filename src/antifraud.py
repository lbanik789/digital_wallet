#! /usr/local/bin/python
import sys
import re


class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name not in self.neighbors:
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)
                self.neighbors = sorted(self.neighbors)
                neighbor.neighbors = sorted(neighbor.neighbors)
        else:
            return False

    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            if isinstance(neighbor, Vertex):
                if neighbor.name not in self.neighbors:
                    self.neighbors.append(neighbor.name)
                    neighbor.neighbors.append(self.name)
                    self.neighbors = sorted(self.neighbors)
                    neighbor.neighbors = sorted(neighbor.neighbors)
            else:
                return False

    def __repr__(self):
        return str(self.neighbors)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            self.vertices[vertex.name] = vertex.neighbors

    def add_vertices(self, vertices):
        for vertex in vertices:
            if isinstance(vertex, Vertex):
                self.vertices[vertex.name] = vertex.neighbors

    def add_edge(self, vertex_from, vertex_to):
        if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
            vertex_from.add_neighbor(vertex_to)
            if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
                self.vertices[vertex_from.name] = vertex_from.neighbors
                self.vertices[vertex_to.name] = vertex_to.neighbors

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def adjacencyList(self):
        if len(self.vertices) >= 1:
            return [str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys()]
        else:
            return dict()

    def adjacencyMatrix(self):
        if len(self.vertices) >= 1:
            self.vertex_names = sorted(g.vertices.keys())
            self.vertex_indices = dict(zip(self.vertex_names, range(len(self.vertex_names))))
            import numpy as np
            self.adjacency_matrix = np.zeros(shape=(len(self.vertices), len(self.vertices)))
            for i in range(len(self.vertex_names)):
                for j in range(i, len(self.vertices)):
                    for el in g.vertices[self.vertex_names[i]]:
                        j = g.vertex_indices[el]
                        self.adjacency_matrix[i, j] = 1
            return self.adjacency_matrix
        else:
            return dict()

import Vertex
import Graph


def graph(g):
    """ Function to print a graph as adjacency list and adjacency matrix. """
    return str(g.adjacencyList()) + '\n' + '\n' + str(g.adjacencyMatrix())




argList = []
batchFile = ''
print "Number of arguments is %s" % len(sys.argv)
argList = sys.argv
print "Argument List: %s" % argList


read_data = []
with open(argList[1], 'rb') as fh:
    read_data = fh.readlines()

g = Graph()

for line in read_data:
    m = re.search(r'^.*?\,\s+(\d+)\,\s+(\d+)\,.*', line)
    if m:
       #print m.group(1)
       #print m.group(2)
       g.add_edge((self, m.group(1),m.group(2)))
       #print "============================="


