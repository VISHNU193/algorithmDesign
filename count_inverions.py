import random as r
import time as t


c3=0

def mergesort(a,l,r):
	n=len(a)
	if n>1:
		mid = (n)//2
		b=a[:mid]
		c=a[mid:]
		print("      ",len(b))
		print("      ",len(c))
		mergesort(b,l,mid-1)
		mergesort(c,mid,r)
		merge(a,b,c)
		
def merge(a,b,c):
	global c3
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
			c3 += len(b)-i
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

num = [2,5,3,7,8,4,1,5,6]
num =[1,5,4,8,10,2,6,9,12,11]
mergesort(num,0,len(num)-1)
print(num)
print(c3)