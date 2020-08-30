list1=[3,9,4,7,5,0,1,6,8,2]
# list1.sort()
print(list1)
def quicksort(list, start, end):
    pivot_index=sort1(list, start, end)
    print(list)
    if start<pivot_index-1:
        quicksort(list, start, pivot_index-1)
        pass
    if pivot_index<end:
        quicksort(list,pivot_index, end)
def sort1(list,start,end):
    pivot_index=int((start+end)/2)
    pivot_value=list[pivot_index]
    print(pivot_index)
    while start<=end:
        while list[start] < pivot_value:
            start = start + 1
            pass
        while list[end] > pivot_value:
            end = end - 1
            pass
        if start<=end:
            temp = list[start]
            list[start] = list[end]
            list[end] = temp
            start=start+1
            end=end-1
    return start

print(quicksort(list1,0,len(list1)-1))


