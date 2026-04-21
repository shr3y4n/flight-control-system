import numpy as np

class KalmanFilter:
    def __init__(self,A,B,C,Q,R):
        self.A=A; self.B=B; self.C=C
        self.Q=Q; self.R=R
        self.P = np.eye(A.shape[0])
        self.x = np.zeros((A.shape[0],1))

    def predict(self,u):
        self.x = self.A@self.x + self.B*u
        self.P = self.A@self.P@self.A.T + self.Q

    def update(self,z):
        K = self.P@self.C.T @ np.linalg.inv(self.C@self.P@self.C.T + self.R)
        self.x = self.x + K@(z - self.C@self.x)
        self.P = (np.eye(len(self.P)) - K@self.C)@self.P