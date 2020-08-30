# 경로탐색에 dfs를 쓰는게 ford_fulkerson
# 경로탐색에 bfs를 쓰는게 edmonds-karp -> 이게 더 빠름
# https://www.programiz.com/dsa/ford-fulkerson-algorithm
# http://blog.naver.com/PostView.nhn?blogId=kks227&logNo=220804885235

graph = [[0, 8, 0, 0, 3, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 7, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 7, 4, 0, 0],
         [0, 0, 0, 0, 0, 0]]

source=0
sink=5

from collections import deque
def ford_fulkerson(graph, source,sink):
  def bfs(source, sink,parent):
    visited=[]
    queue=deque([source])

    while queue:
      item=queue.popleft()
      if item not in visited:
        visited.append(item)
        for i in range(len(graph[item])):
          if i!=item and i not in visited and graph[item][i]>0:
            queue.append(i)
            parent[i]=item
    return True if sink in visited else False

  parent=[-1]*len(graph)
  max_flow=0

  while bfs(source,sink,parent):
    path_flow=float("inf")
    s=sink
    while s!=source:
      path_flow=min(path_flow, graph[parent[s]][s])
      s=parent[s]
    max_flow=max_flow+path_flow
    v=sink
    while v!=source:
      u=parent[v]
      graph[u][v]=graph[u][v]-path_flow
      graph[v][u] = graph[v][u] + path_flow
      v=parent[v]
  return max_flow

print(ford_fulkerson(graph,source,sink))