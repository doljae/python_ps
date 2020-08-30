# https://www.fun-coding.org/Chapter20-shortest-live.html
import heapq

mygraph = {
  'A': {'B': 8, 'C': 1, 'D': 2},
  'B': {},
  'C': {'B': 5, 'D': 2},
  'D': {'E': 3, 'F': 5},
  'E': {'F': 1},
  'F': {'A': 5}
}

parents={}
for item in mygraph:
  if item not in parents:
    parents[item]=None

def dijkstra(graph, parents, start):
  distances = {node: float("inf") for node in graph}
  distances[start] = 0
  queue = []
  heapq.heappush(queue, [distances[start], start])

  while queue:
    current_distance, current_node = heapq.heappop(queue)
    if distances[current_node] < current_distance:
      continue
    for adjacent, weight in graph[current_node].items():
      distance = current_distance + weight
      if distance < distances[adjacent]:
        distances[adjacent] = distance
        heapq.heappush(queue, [distance, adjacent])
        parents[adjacent]=current_node
  return distances


print(dijkstra(mygraph, parents, "A"))

def print_path(parents,start,end):
  result=[]
  cur=end
  while cur!=start:
    result.append(cur)
    cur=parents[cur]
  result.append(start)
  return list(reversed(result))

print(print_path(parents,"A","F"))