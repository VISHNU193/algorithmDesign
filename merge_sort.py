import random as r
import time as t
import matplotlib.pyplot as plt
def mergesort(a,l,r):
	n=len(a)
	if n>1:
		mid = (n)//2
		b=a[:mid]
		c=a[mid:]
		mergesort(b,l,mid-1)
		mergesort(c,mid,r)
		merge(a,b,c)
		
def merge(a,b,c):
	n1 = len(b)
	n2 = len(c)
	
	i=j=k=0
	
	while i<n1 and j<n2:
		if b[i] <c[j] :
			a[k] = b[i]
			i += 1
			k +=1
		else:
			a[k] = c[j]
			j += 1
			k += 1
	while i< n1:
		a[k] = b[i]
		i += 1
		k +=1
	while j<n2:
		a[k] = c[j]
		j += 1
		k += 1


timelist = []
numlist =[100,200,300,500,1000,2000,3000,5000,6000,8000,10000,50000]
for n in numlist:
	arr = [r.randint(0,n) for x in range(n)]
	t1 = t.perf_counter()
	mergesort(arr,0,len(arr)-1)
	t2 = t.perf_counter()
	#print(arr)
	timelist.append(t2-t1)

print(numlist)
print()
print(timelist)				
print()
arr = [r.randint(0,100) for x in range(100)]
mergesort(arr,0,len(arr)-1)

plt.plot(numlist,timelist)
plt.xlabel("Input size")
plt.ylabel("Time taken")
plt.title("Merge Sort")
plt.show()