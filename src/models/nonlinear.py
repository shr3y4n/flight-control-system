import numpy as np

A = np.array([[0, 1],
              [-0.5, -0.8]])

B = np.array([[0],
              [1]])   # ← MUST be column vector

def dynamics(x, u):
    x = np.array(x).reshape(-1, 1)
    dx = A @ x + B * u
    return dx.flatten()