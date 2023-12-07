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
  # Initialize the parent dictionary to store the parent of each vertex
  parent = {vertex: None for vertex in graph}

  # Queue for BFS
  queue = deque([source])

  # Set the parent of the source vertex to itself
  parent[source] = source

  while queue:
      current_vertex = queue.popleft()

      for neighbor in graph[current_vertex]:
          # Check if the neighbor has not been visited
          if parent[neighbor] is None:
              # Set the parent of the neighbor to the current vertex
              parent[neighbor] = current_vertex
              queue.append(neighbor)

  return parent

def get_sample_graph():
   return {'s': {'a', 'b'},
          'a': {'b'},
          'b': {'c'},
          'c': {'a', 'd'},
          'd': {}
          }

def test_get_path():
  graph = get_sample_graph()
  parents = bfs_path(graph, 's')
  assert get_path(parents, 'd') == 'sbc'
    
def get_path(parents, destination):
  path = ""
  current_node = destination

  while parents[current_node] != current_node:
    current_node = parents[current_node]
    path = path + current_node

  path2 = path[::-1]
  return path2
