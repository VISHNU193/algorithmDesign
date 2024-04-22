import time


def linearSearch(arr,key):
    for i in range(len(arr)):
        if(arr[i]==key):
            return i

    return None

numlist = [3,5,45,23,435,65,7,67,-234,-60,-98,2,2,2,2]
key = 100
t1 = time.time_ns()
index = linearSearch(numlist, key)
t2= time.time_ns()
print(f"Index at which {key} is present in list is {index} ")
print(t2-t1)

