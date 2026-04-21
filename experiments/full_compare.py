import numpy as np
import matplotlib.pyplot as plt

from src.controllers.pid import PID
from src.controllers.lqr import LQR
from src.controllers.mpc import MPC
from src.simulation.engine import simulate

A = np.array([[0,1],[-0.5,-0.8]])
B = np.array([[0],[1]])

pid = PID(12,2,3)
lqr = LQR(A,B,np.diag([10,1]),np.array([[1]]))
mpc = MPC(A,B,np.diag([10,1]),np.array([[1]]))

pid_data = simulate(pid)
lqr_data = simulate(lqr)
mpc_data = simulate(mpc)

plt.plot(pid_data[:,0], pid_data[:,1], label="PID")
plt.plot(lqr_data[:,0], lqr_data[:,1], label="LQR")
plt.plot(mpc_data[:,0], mpc_data[:,1], label="MPC")

plt.legend()
plt.show()