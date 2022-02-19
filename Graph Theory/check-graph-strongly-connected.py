# We want to check if graph is strongly connected or not.

"""
Kosaraju's DFS based simple algorithm that does two DFS traversals of graph


1) Initialize all vertices as not visited.
2) Do a DFS traversal of graph starting from any arbitrary vertex v. 
    If DFS traversal doesn't visit all vertices, then return false.

3) Reverse all arcs (or find transpose or reverse of graph) 
4) Mark all vertices as not-visited in reversed graph.
5) Do a DFS traversal of reversed graph starting from same vertex v (Same as step 2). 
    If DFS traversal doesn't visit all vertices, then return false. Otherwise return true.

The idea is, if every node can be reached from a vertex v, and every node can reach v, then the graph is strongly connected. 
In step 2, we check if all vertices are reachable from v. In step 4, we check if all vertices can reach v

"""

"""
Time Complexity : O(V*(V+E)) 
"""
 
from collections import defaultdict

class Graph:
 
    def __init__(self, vertices):
        self.vertices = vertices  # No. of vertices
        self.graph = defaultdict(list)  

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def traverseGraph(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.traverseGraph(i, visited)


    def isSC(self):

        visited = [False for v in self.vertices]

        # traverse the graph and update visited
        self.traverseGraph(0, visited)

        for i in visited:
            if not i:
                return False;






# Test your Graph class implementation here
g1 = Graph(5)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.addEdge(3, 0)
g1.addEdge(2, 4)
g1.addEdge(4, 2)
print ("Yes" if g1.isSC() else "No")
 
g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print ("Yes" if g2.isSC() else "No") 