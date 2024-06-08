import random as r
import matplotlib.pyplot as plt
import time as t

def selection_sort(array: list[int]):
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

def insertion_sort(array: list[int]):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def merge_sort(array: list[int]):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        merge(array, left_half, right_half)

def merge(array: list[int], left_half: list[int], right_half: list[int]):
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1

def time_sort(sort_func, array: list[int]) -> float:
    start = t.perf_counter()
    sort_func(array)
    end = t.perf_counter()
    return end - start

r.seed(42)  # For reproducibility
numlist = [100, 200, 300, 500, 1000, 2000, 3000, 5000, 6000, 10000, 50000]
sel_time = []
inst_time = []
merg_time = []

for n in numlist:
    array = [r.randint(0, n) for _ in range(n)]
    sel_time.append(time_sort(selection_sort, array.copy()))
    inst_time.append(time_sort(insertion_sort, array.copy()))
    merg_time.append(time_sort(merge_sort, array.copy()))

print(inst_time)
print(sel_time)
print(merg_time)

plt.plot(numlist, merg_time, label="MergeSort")
plt.plot(numlist, sel_time, label="SelectionSort")
plt.plot(numlist, inst_time, label="InsertionSort")
plt.xlabel("Input Size")
plt.ylabel("Time Taken (s)")
plt.title("Comparing Sorting Algorithms")
plt.legend()
plt.yscale('log')  # If time differences are large, consider using log scale
plt.show()


