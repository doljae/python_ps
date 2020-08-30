#이분 매칭, bipartite matching
import sys
input = sys.stdin.readline
def dfs(start):
  if visit[start]==1:
    return False
  visit[start]=1
  for i in s[start]:
    if d[i]==0 or dfs(d[i]) is True:
      d[i]=start
      return True
  return False

test=int(input())
for i in range(test):
  n, m = map(int, input().split())
  s = [[] for i in range(m + 1)]
  d = [0 for i in range(n + 1)]
  cnt=0
  for j in range(1, m + 1):
    a, b = map(int, input().split())
    for k in range(a, b + 1):
      s[j].append(k)
  # print(s,d)

  for j in range(1, m + 1):
    visit = [0 for i in range(m + 1)]
    if dfs(j):
      cnt += 1
  print(cnt)

