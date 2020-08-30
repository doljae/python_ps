# https://bcp0109.tistory.com/entry/%EC%9C%84%EC%83%81%EC%A0%95%EB%A0%AC-Topological-Sort-Java?category=848939
# 위상 정렬, DFS나 indegree배열을 사용함
# indegree 배열이 일반적
from collections import deque

graph = {
    1: {2, 3},
    2: {4, 5},
    3: {4, 7},
    4: {6},
    5: {4, 6},
    6: {},
    7: {}
}
indegree = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0
}
for item in graph:
    for item2 in graph[item]:
        indegree[item2] += 1

queue1=deque([])
result=[]

for item in indegree:
    if indegree[item]==0:
        queue1.append(item)

while queue1:
    item=queue1.popleft()
    result.append(item)
    for item2 in graph[item]:
        indegree[item2]-=1
        if indegree[item2]==0:
            queue1.append(item2)
if len(result)!=len(graph):
    print("cycle exist!")
print(queue1,result)




