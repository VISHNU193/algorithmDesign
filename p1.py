import matplotlib.pyplot as plt
import numpy as np

x = []
fn = []
cgn = []

for n in range(0, 1001):
    x.append(n)
    fn.append(7*n+5)
    cgn.append(8*n)

x_points = np.array(x)
fnArray = np.array(fn)
cgnArray = np.array(cgn)

plt.plot(x_points, fnArray, cgnArray)
plt.title("O(f(n)) where f(n) = 7*n+5")
plt.xlabel("number of instructions")
plt.ylabel("number of operations")
plt.legend(["f(n)=7*n+5", "cg(n)=8*n"], loc="lower right")
plt.show()
