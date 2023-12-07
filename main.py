from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
  # Initialize distances and number of edges for each vertex
  distances = {vertex: (float('inf'), float('inf')) for vertex in graph}
  distances[source] = (0, 0)  # Distance from source to itself is 0 with 0 edges

  for k in graph:
      for i in graph:
          for j, weight in graph[i]:
              # Check if the weight is 0 or if the new path is shorter
              if distances[i][0] + weight < distances[j][0] or (weight == 0 and distances[i][1] + 1 < distances[j][1]):
                  distances[j] = (distances[i][0] + weight, distances[i][1] + 1)

  return distances
    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    pass

def get_sample_graph():
   return {'s': {'a', 'b'},
          'a': {'b'},
          'b': {'c'},
          'c': {'a', 'd'},
          'd': {}
          }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    pass

