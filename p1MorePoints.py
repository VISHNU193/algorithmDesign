
import numpy as np
import matplotlib.pyplot as plt

# x2_points = np.array([x for x in range(1000,20000,1000)])
x1_points = np.longdouble(np.linspace(1000,20000,100))
# x2_points = np.array([x for x in range(1000, 20000 , 2000)])

# x1_points = np.array([x for x in range(1000,20000,1000)])
# ol = 0.15

def logarithm(n):
    return np.log(n)


def linear(n):
    return n


def quad(n):
    return n**2


def cube(n):
    return n**3


def linearLog(n):
    return n*np.log(n)


def exponential(n):
    result = np.array([])
    for x in n:
        result = np.append(result, 2**x)

    return result


def factorial(n):
    result = np.array([])
    for ele in n:
        temp = 1
        for i in range(1,ele+1):
            temp = temp * i
        result = np.append(result , temp)

    return result

# print(2**10000)
print()
plt.plot(x1_points,logarithm(x1_points),label="O(log(n))")
plt.plot(x1_points,linear(x1_points),label="O(n)")
plt.plot(x1_points,linearLog(x1_points),label="O(n*log(n)")
plt.plot(x1_points,quad(x1_points),label="O(n^2)")
plt.plot(x1_points,cube(x1_points),label="O(n^3)")
# plt.plot(x1_points,exponential(x1_points),label="O(2^n)")
# plt.plot(x2_points,factorial(x2_points),label="O(n!)")

plt.legend()
plt.show()


