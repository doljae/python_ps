# https://www.geeksforgeeks.org/bellman-ford-algorithm-simple-implementation/

mygraph = {
  'A': {'B': 8, 'C': 1, 'D': 2},
  'B': {},
  'C': {'B': 5, 'D': 2},
  'D': {'E': 3, 'F': 5},
  'E': {'F': 1},
  'F': {'A': 5}
}
mygraph2=[]
for item in mygraph:
  for item2 in mygraph[item]:
    mygraph2.append([item,item2,mygraph[item][item2]])
# print(mygraph2)
def bellman(graph, graph2, start):
  dist={}
  for item in graph:
    dist[item]=float("inf")
  dist[start]=0

  for i in range(len(dist) - 1):
    for item in graph2:
      start = item[0]
      end = item[1]
      weight = item[2]
      if dist[start] + weight < dist[end]:
        dist[end] = dist[start] + weight

  for item in graph2:
    start = item[0]
    end = item[1]
    weight = item[2]
    if dist[start] != float("inf") and dist[start] +weight < dist[end]:
      print("Graph contains negative weight cycle")

  print("Vertex Distance from Source")
  for item in dist:
    print(item,"\t\t" ,dist[item])

  return dist

print(bellman(mygraph,mygraph2,"A"))