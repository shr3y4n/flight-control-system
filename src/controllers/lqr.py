import numpy as np
from scipy.linalg import solve_continuous_are

class LQR:
    def __init__(self, A, B, Q, R):
        P = solve_continuous_are(A, B, Q, R)
        self.K = np.linalg.inv(R) @ B.T @ P

    def compute(self, x, ref, dt):
        x = np.array(x).reshape(-1, 1)

        # reference tracking
        ref_vec = np.array([[ref], [0]])

        u = -self.K @ (x - ref_vec)

        return u.item()