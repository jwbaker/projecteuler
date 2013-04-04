'''
Created on 2013-04-02

Problem 18:
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23:

*3*
*7* 4
2 *4* 6
8 5 *9* 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67 is the same
challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method!

SOLUTION: 1074
@author: Jason Baker
'''

# This problem seemed stupidly hard at first, but then it became quite easy once I thought it through
def triangle():
    return [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]];

# Define an Edge relation class
# u is the starting point (near the top of the triangle)
# v is the end point (near the bottom of the triangle)
# w is the weight of the edge
# Note that w is negative here; this will become important
class Edge:
    def __init__(self, u, v, w):
        self.u = u;
        self.v = v;
        self.w = -1 * w;

# Because of the way graphs work, I had to modify the triangle slightly
# Effectively, I just added a one-element row to the very top, with 0 values
# That allowed me to think of the numbers in the triangle as weights of the paths between nodes on a graph
def toGraph(triangle):
    graph = [None] * len(triangle);
    
    nextIndex = 1;
    for i in range(0, len(triangle)):
        graph[i] = [None] * len(triangle[i]);
        for j in range(0, len(triangle[i])):
            graph[i][j] = [nextIndex, triangle[i][j]];
            nextIndex += 1;
    return [[[0, 0]]] + graph;

def vertices(graph):
    vertices = [];
    
    for i in range(0, len(graph)):
        for j in range(0, len(graph[i])):
            vertices.append(graph[i][j][0]);
    return vertices;

def edges(graph):
    edges = [];
    
    for i in range(0, len(graph) - 1):
        for j in range(0, len(graph[i])):
            edges.append(Edge(graph[i][j][0], graph[i + 1][j][0], graph[i + 1][j][1]));
            
            if i > 0:
                edges.append(Edge(graph[i][j][0], graph[i + 1][j + 1][0], graph[i + 1][j + 1][1]));
    return edges;

# An implementation of the Bellman-Ford algorithm for the shortest path through a graph
# "Shortest path?" you may be asking. "But I thought the problem was a longest path one?"
# It is, but shortest path is easier
# And as it turns out, you can turn a longest path problem into a shortest path problem by negating all of the edge weights
# The Bellman-Ford algorithm is specifically designed to handle negative weights, which is why I can't use Dijkstra's algorithm
def bellmanFord(vertices, edges, start = 0):
    infinity = 1000000;
    dist = [infinity] * len(vertices);
    dist[start] = 0;
    
    for i in range(1, len(vertices) - 1):
        for e in edges:
            if dist[e.u] + e.w < dist[e.v]:
                dist[e.v] = dist[e.u] + e.w;
                
    return dist;

# Because the B-F algorithm returns a list of the shortest paths to each node of the graph, from the start (my imaginary node, in this case),
# I'm only interested in the very last row, so just find the smallest one there, and negate it
def longestCompletePath(paths):
    lastRow = len(triangle());
    
    smallest = 0;
    
    for p in paths[len(paths) - lastRow:]:
        if p < smallest:
            smallest = p;
    return -1 *smallest;
    
graph = toGraph(triangle());
vertices = vertices(graph);
edges = edges(graph);

paths = bellmanFord(vertices, edges);

print(longestCompletePath(paths));