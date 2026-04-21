import numpy as np
import matplotlib.pyplot as plt
import os

from src.controllers.pid import PID
from src.controllers.lqr import LQR
from src.controllers.mpc import MPC
from src.simulation.engine import simulate
from src.simulation.metrics import overshoot, settling_time
from src.visualization.animation import animate_pitch

# ensure results folder exists
os.makedirs("results/plots", exist_ok=True)

# -----------------------------
# System
# -----------------------------
A = np.array([[0, 1],
              [-0.5, -0.8]])

B = np.array([[0],
              [1]])

# -----------------------------
# Controllers
# -----------------------------
Q = np.diag([100, 20])
R = np.array([[3]])

pid = PID(50, 10, 15)
lqr = LQR(A, B, Q, R)

Q_mpc = np.diag([80, 15])
R_mpc = np.array([[10]])
mpc = MPC(A, B, Q_mpc, R_mpc, N=10)

# -----------------------------
# Simulation
# -----------------------------
print("Running PID...")
pid_data = simulate(pid)

print("Running LQR...")
lqr_data = simulate(lqr)

print("Running MPC...")
mpc_data = simulate(mpc)

# -----------------------------
# Plot: State
# -----------------------------
plt.figure()
plt.plot(pid_data[:,0], pid_data[:,1], label="PID")
plt.plot(lqr_data[:,0], lqr_data[:,1], label="LQR")
plt.plot(mpc_data[:,0], mpc_data[:,1], label="MPC")
plt.plot(pid_data[:,0], pid_data[:,4], '--', label="Reference")
plt.legend()
plt.title("Pitch Angle Response")
plt.savefig("results/plots/state_comparison.png")
plt.close()

# -----------------------------
# Plot: Control
# -----------------------------
plt.figure()
plt.plot(pid_data[:,0], pid_data[:,3], label="PID")
plt.plot(lqr_data[:,0], lqr_data[:,3], label="LQR")
plt.plot(mpc_data[:,0], mpc_data[:,3], label="MPC")
plt.legend()
plt.title("Control Effort")
plt.savefig("results/plots/control_comparison.png")
plt.close()

# -----------------------------
# Metrics
# -----------------------------
print("\n--- METRICS ---")
print("PID Overshoot:", overshoot(pid_data[:,1]))
print("LQR Overshoot:", overshoot(lqr_data[:,1]))
print("MPC Overshoot:", overshoot(mpc_data[:,1]))

# -----------------------------
# Animation
# -----------------------------
print("\nCreating animation...")
animate_pitch(mpc_data)