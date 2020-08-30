import heapq

queue=[]
graph_data = [[2, 'A'], [5, 'B'], [3, 'C']]

for edge in graph_data:
  heapq.heappush(queue,edge)

for index in range(len(queue)):
  print(heapq.heappop(queue))

print(queue)

from collections import defaultdict
list_dict=defaultdict(list)
print(list_dict["key1"])

from collections import defaultdict
from heapq import *

myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

# eloge 해결법
def prim(start_node, edges):
  mst=list()
  adjacent_edges=defaultdict(list)
  for weight, n1, n2 in edges:
    adjacent_edges[n1].append((weight,n1,n2))
    adjacent_edges[n2].append((weight,n2,n1))

  connected_nodes=set(start_node)
  candidate_edge_list=adjacent_edges[start_node]
  heapify(candidate_edge_list)

  while candidate_edge_list:
    weight,n1,n2=heappop(candidate_edge_list)
    if n2 not in connected_nodes:
      connected_nodes.add(n2)
      mst.append((weight,n1,n2))

      for edge in adjacent_edges[n2]:
        if edge[2] not in connected_nodes:
          heappush(candidate_edge_list,edge)
  return mst

print(prim("A",myedges))

from heapdict import heapdict

# 하시발존나어려운데 이게 elogv임
def prim2(graph, start):
  mst=list()
  edge_weights=heapdict()
  parents=dict()
  total_weight=0

  for node in graph.keys():
    edge_weights[node]=float("inf")
    parents[node]=None

  edge_weights[start]=0
  parents[start]=start

  while edge_weights:
    current_node, current_weight=edge_weights.popitem()
    mst.append([parents[current_node],current_node,current_weight])
    total_weight+=current_weight
    for adjacent,weight in graph[current_node].items():
      if adjacent in edge_weights and weight<edge_weights[adjacent]:
        edge_weights[adjacent]=weight
        parents[adjacent]=current_node
  return mst,total_weight

mygraph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}
mst, total_weight = prim2(mygraph, 'A')
print ('MST:', mst)
print ('Total Weight:', total_weight)