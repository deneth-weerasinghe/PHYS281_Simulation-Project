import numpy as np
import os

list_1 = [0, 1, 2, 3, 4, 5]

my_list = []
x = ["t"] + [i for i in list_1]
my_list.append(x)
# print(my_list)

b = "Christmas"
# print(b.lower())

# x_1 = np.array([1, 1, 1])
# x_2 = np.array([1, 1, 1])

# print(x_2 - x_1)

c = []
x = [[0], [1], [2], [3]]
y = [[0], [1], [2], [3]]

f = []

# f.append(x)
# f.append(y)
# print(x + y)

for i in range(len(x)):
    f.append([x[i], y[i]])
for i in f:
    print(i)