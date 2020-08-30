def next_perm(arr):
    i,j=len(arr)-1,len(arr)-1
    # 순열 뒤에서 i인덱스가 가르키는 값이 i-1이 가르키는 값보다 작을 때 까지 i을 -1 해줌
    while i>0 and arr[i-1]>=arr[i]:
        i-=1
    # 현재 i는 반복문이 안 돌았기 때문에 -1을 해줌, 이래야 arr[i]<arr[i-1] 이 되는 가장 큰 i가 됨
    i-=1
    # i가 0이란 것은 i인덱스가 가르키는 값이 i-1이 가르키는 값보다 항상 컸기 때문인데,
    # 그럼 5,4,3,2,1 이런 식이라는 것이므로 다음 사전순 순열이 존재하지 않음, false 반환
    if i==0:
        return False
    #i가 정해지면 arr 맨 뒤에서 부터 arr[i] 보다 큰 값을 가지는 index j 를 찾아낸다
    while arr[i]>=arr[j]:
        j-=1
    # 둘을 스왑한다
    arr[i], arr[j]=arr[j],arr[i]
    # i+1 ~ len(arr) -1 까지의 값들을 전부 스왑한다
    i+=1
    k=len(arr)-1
    while i<k:
        arr[i], arr[k]=arr[k],arr[i]
        i+=1
        k-=1
    return arr

# arr=next_perm([2,5,1,9,7])
# print(arr)
# arr=next_perm(arr)
# print(arr)
# arr=next_perm(arr)
# print(arr)

arr=next_perm([3,4,1,4,5])
print(arr)
arr=next_perm(arr)
print(arr)
arr=next_perm(arr)
print(arr)