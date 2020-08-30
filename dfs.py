from collections import deque

graph_list={0:set([1]),1:set([0,2,3]),2:set([1,3,4]),
            3:set([1,2,4,5]),4:set([2,3]),5:set([3,6,7]),
            6:set([5,8]),7:set([5]),8:set([6])}

print(graph_list)

def dfs_stack(graph_list,root):
    visited=[]
    stack1=[root]
    while stack1:
        pop_num=stack1.pop()
        if pop_num not in visited:
            visited.append(pop_num)
            # stack에 들어있는 node도 제외하고 넣어주기
            stack1+=graph_list[pop_num]-(set(visited)|set(stack1))
        pass
    return visited

visited = []
def dfs_recursive(graph_list, root):
    visited.append(root)
    for i in graph_list[root]:
        if i not in visited:
            dfs_recursive(graph_list,i)
    return visited

print(dfs_stack(graph_list,0))
print(dfs_recursive(graph_list,0))

# def DFS_visit(adj, u, visited):
#     visited.append(u)
#     for v in adj[u]:
#         if v not in visited:
#             DFS_visit(adj, v, visited)
#
#
# def DFS(adj, s):
#     visited = []
#     DFS_visit(adj, s, visited)
#     return visited
# print(DFS(graph_list, 0))
