

n = int(input("Enter the number of items : "))
weight=[None]
for i in range(1,n+1):
    weight.append(int(input(f"Enter weight of item {i}: ")))

W = int(input("Enter maximum weight : "))


OPT = [[None]*(W+1) for _ in range(n+1)]
for w in range(0, W+1):
    OPT[0][w] = 0
for i in range(0, n+1):
    OPT[i][0] = 0


for i in range(1, n+1):
    for w in range(1, W+1):
        if weight[i] > w:
            OPT[i][w] = OPT[i-1][w]
            
        else:
            OPT[i][w] = max( OPT[i-1][w], weight[i]+OPT[i-1][w-weight[i]])


print(f"MAX : {OPT[n][W]}")
result = set()
i = n
k = W
while i > 0:
    if OPT[i][k] != OPT[i-1][k]:
        result.add(i)
        k = k - weight[i]
    i = i-1

print("Resulting set : ", result)
