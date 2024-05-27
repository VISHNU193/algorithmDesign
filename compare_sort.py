import random as r
import matplotlib.pyplot as plt
import time as t


def selection_sort(a:list[int]):
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if a[min]>a[j]:
                min = j

        a[i],a[min] = a[min],a[i]
def insertion_sort(a:list[int]):
    for i in range(1,len(a)):
        key = a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j = j-1
        a[j+1]=key


def mergeSort(a:list[int]):
    n = len(a)
    if n>1:
        mid = n//2
        b = a[mid:]
        c = a[:mid]
        mergeSort(b)
        mergeSort(c)
        merge(a,b,c)

def merge(a:list,b:list,c:list):
    n1 = len(b)
    n2 = len(c)

    i=j=k=0

    while i<n1 and j<n2:
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
            k += 1
        else:
            a[k] = c[j]
            j+=1
            k+=1
    while i<n1:
        a[k] = b[i]
        i += 1
        k += 1
    while j<n2:
        a[k] = c[j]
        j += 1
        k += 1


numlist = [100,200,300,500,1000,2000,3000,5000,6000,10000,50000]

sel_time=[]
inst_time=[]
merg_time=[]

for n in numlist:
    arr = [r.randint(0, n) for _ in range(n)]
    t1 = t.perf_counter()
    selection_sort(arr)
    t2 = t.perf_counter()
    sel_time.append(t2-t1)
    print(n)
for n in numlist:
    arr = [r.randint(0, n) for _ in range(n)]
    t1 = t.perf_counter()
    insertion_sort(arr)
    t2 = t.perf_counter()
    inst_time.append(t2-t1)
    print(n)
for n in numlist:
    arr = [r.randint(0, n) for _ in range(n)]
    t1 = t.perf_counter()
    mergeSort(arr)
    t2 = t.perf_counter()
    merg_time.append(t2-t1)
    print(n)

plt.plot(numlist,merg_time,label="MergeSort")
plt.plot(numlist,sel_time,label="SelectionSort")
plt.plot(numlist,inst_time,label="InsertionSort")
plt.xlabel("Input size")
plt.ylabel("TIme Taken")
plt.title("Comparing Sorts")
plt.legend()
plt.show()

print(inst_time)
print(sel_time)
print(merg_time)
