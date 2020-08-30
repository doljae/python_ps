from sys import maxsize

vertex_num = 4
INF = maxsize

def print_solution(distance):
  for i in range(vertex_num):
    for j in range(vertex_num):
      if (distance[i][j] == INF):
        print("INF", end=" ")
      else:
        print(distance[i][j], end="  ")
    print(" ")


def floydWarshall(graph):
  dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
  for k in range(vertex_num):
    for i in range(vertex_num):
      for j in range(vertex_num):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  print_solution(dist)


graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]

floydWarshall(graph)
