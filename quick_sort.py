import random as r

def quickSort(a:list[int],l,r):
    if l<r:
        s = partition(a,l,r)
        quickSort(a,l,s-1)
        quickSort(a,s+1,r)
def partition(arr:list[int],l,r):
    p = arr[l]
    i = l+1
    j = r
    while True:
        while i<=j and arr[j]>= p:
            j = j-1
        while i<=j and arr[i] <= p:
            i += 1

        if i<=j :
            arr[i],arr[j]= arr[j],arr[i]
        else:
            break
    arr[l],arr[j]= arr[j],arr[l]
    return j
numInput = [1, 10, 3, 16, 14, 5, 15, 4, 13, 0]
print(numInput)
quickSort(numInput,0, len(numInput)-1)
print(numInput)