import time

numList = [-234, -98, -60, 2, 2, 2, 2, 3, 5, 7, 23, 45, 65, 67, 435]


def binarySearch(arr, ke, low, high):

    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == ke:
            return mid
        elif arr[mid] > ke:
            return binarySearch(arr, ke, low, mid - 1)
        else:
            return binarySearch(arr, ke, mid + 1, high)
    else:
        return None


key = 100
t1 = time.time_ns()
index = binarySearch(numList, key, 0, len(numList))
t2 = time.time_ns()
print(f"Index at which {key} is present in list is {index} ")
print(t2 - t1)
