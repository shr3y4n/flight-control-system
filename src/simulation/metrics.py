import numpy as np

def overshoot(y):
    return np.max(y) - y[-1]

def settling_time(y, tol=0.02):
    final=y[-1]
    for i in range(len(y)):
        if np.all(np.abs(y[i:]-final)<tol):
            return i