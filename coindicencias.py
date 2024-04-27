import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1, 2, 3, 4, 5, 6])

def conv(a,b):
    convolution = []
    for i in range(len(a)):
        for j in range(len(b)):
            convolution.append(a[i]+b[j])
    return list(sorted(convolution))


