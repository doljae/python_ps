list1=[3,9,4,7,5,0,1,6,8,2]
result=[]
def mergeSort(list):
    if len(list)>1:
        middle = int((0 + len(list)) / 2)
        left = mergeSort(list[:middle])
        right = mergeSort(list[middle:])
        return merge(left, right)
    else:
        return list


def merge(left,right):
    i=0
    j=0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1

    if i==len(left):
        result+=right[j:]
    else:
        result+=left[i:]
    return result

print(mergeSort(list1))


