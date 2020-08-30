list1=[1,2,3,4,5]
n=5
r=3
result=[]
result_flag=[0]*n
selected=[0]*n
def perm(cnt):
    if cnt==r:
        print(result)
        print(result_flag)
        return
    for i in range(n):
        if selected[i]==1:
            continue
        selected[i]=1
        result.append(list1[i])
        result_flag[i]=1
        perm(cnt+1)
        selected[i]=0
        result.remove(list1[i])
        result_flag[i] = 0
perm(0)
result=[]
result_flag=[0]*n
def comb(cnt,start):
    global result
    if cnt==r:
        print(result)
        print(result_flag)
        return
    for i in range(start,n):
        result.append(list1[i])
        result_flag[i]=1
        comb(cnt+1,i+1)
        result.remove(list1[i])
        result_flag[i] = 0
print("=========================")
comb(0,0)