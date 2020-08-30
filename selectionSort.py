list1=[3,5,4,2,1]
print(list1)
def selectionSort1(list):
    length=len(list)
    min_index=0
    start=0
    while start!=length:
        min = list[start]
        for i in range(start,length):
            if min >= list[i]:
                min = list[i]
                min_index = i
        temp = list[min_index]
        list[min_index] = list[start]
        list[start] = temp
        start = start + 1
        print(list)
# selectionSort1(list1)

def selectionSort2(list,start):
    if start<len(list)-1:
        min_index=start
        for i in range(start, len(list)):
            if list[i]<list[min_index]:
                min_index=i
        temp = list[min_index]
        list[min_index] = list[start]
        list[start] = temp
        selectionSort2(list,start+1)
    pass
selectionSort2(list1,0)
print(list1)
