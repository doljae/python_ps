from collections import deque

graph_list={0:set([1]),1:set([0,2,3]),2:set([1,3,4]),
            3:set([1,2,4,5]),4:set([2,3]),5:set([3,6,7]),
            6:set([5,8]),7:set([5]),8:set([6])}

print(graph_list)

def bfs(graph_list, root):
    # 리스트
    visited=[]

    # deque
    queue=deque([root])
    while queue:
        pop_num=queue.popleft()
        if pop_num not in visited:
            # deque에 원소를 추가
            visited.append(pop_num)
            # deque += set - set??
            # deque와 set의 연산이 가능한가?
            queue+=graph_list[pop_num]-(set(visited)|set(queue))
            pass
        pass
    return visited

print(bfs(graph_list,0))
