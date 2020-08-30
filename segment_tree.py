import math

arr1 = [3, 5, 6, 7, 2, 9, 4, 5, 2, 8, 1, 5]
temp = math.ceil(math.log2(len(arr1)))
tree_length = pow(2, temp+1)
tree1 = [0 for i in range(tree_length)]
lazy1=[0 for i in range(tree_length)]
def init(arr1, tree1, node, start, end):
    # print(start,end,node)
    # print(arr1[start],tree1[node])
    if start == end:
        tree1[node] = arr1[start]
        return tree1[node]

    mid = (start + end) // 2
    tree1[node] = init(arr1, tree1, node * 2, start, mid) + init(arr1, tree1, node * 2 + 1, mid + 1, end)
    return tree1[node]

def update(tree1, node, start, end, index, diff):
    if index<start or index>end:
        return
    tree1[node]+=diff
    if start!=end:
        mid=(start+end)//2
        update(tree1,node*2,start,mid,index,diff)
        update(tree1,node*2+1,mid+1,end,index,diff)
    pass

def sum(tree1, node, start,end,left,right):
    update_lazy(tree1,lazy1,node,start,end)
    if left>end or right<start:
        return 0;
    if left<=start and right>=end:
        return tree1[node]
    mid=(start+end)//2
    return sum(tree1,node*2,start,mid,left,right)+sum(tree1,node*2+1,mid+1,end,left,right)
def update_lazy(tree1,lazy1,node,start,end):
    print(node,start,end)
    print(len(lazy1))
    if lazy1[node]==0:
        return
    tree1[node]+=(end-start+1)*lazy1[node]
    if start!=end:
        lazy1[node*2]+=lazy1[node]
        lazy1[node*2+1]+=lazy1[node]
    lazy1[node]=0
def update_range(tree1,lazy1,node,start,end,left,right,val):
    update_lazy(tree1,lazy1,node,start,end)

    if left>end and right<start:
        return
    if left<=start and right>=end:
        tree1[node]+=(end-start+1)*val
        if start!=end:
            lazy1[node*2]+=val
            lazy1[node*2+1]+=val
        return
    mid=(start+end)//2
    update_range(tree1,lazy1,node*2,start,mid,left,right,val)
    update_range(tree1,lazy1,node*2+1,mid+1,end,left,right,val)

    tree1[node]=tree1[node*2]+tree1[node*2+1]

init(arr1, tree1, 1, 0, len(arr1) - 1)
print(tree1)
lazy1[2]+=1
lazy1[4]+=1

update_range(tree1,lazy1,1,0,len(arr1)-1,3-1,5-1,1)
# print(tree1)
# a=sum(tree1,1,0,len(arr1)-1,8,11)
# print(a)