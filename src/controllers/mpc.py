import numpy as np
from scipy.linalg import solve_discrete_are

class MPC:
    def __init__(self, A, B, Q, R, N=10, dt=0.01):
        self.N = N
        self.Q = Q
        self.R = R

        # Discretize (simple Euler is fine here)
        self.Ad = np.eye(A.shape[0]) + A * dt
        self.Bd = B * dt

        # Precompute terminal LQR gain (stabilizing)
        P = solve_discrete_are(self.Ad, self.Bd, Q, R)
        self.K = np.linalg.inv(self.Bd.T @ P @ self.Bd + R) @ (self.Bd.T @ P @ self.Ad)

    def compute(self, x, ref, dt):
        x = np.array(x).reshape(-1, 1)
        ref_vec = np.array([[ref], [0]])

        # finite-horizon-style control using stabilizing gain
        u = -self.K @ (x - ref_vec)

        # clamp actuator (important)
        u = np.clip(u.item(), -10, 10)

        return u