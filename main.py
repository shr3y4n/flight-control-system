import numpy as np
import matplotlib.pyplot as plt

from src.controllers.pid import PID
from src.controllers.lqr import LQR
from src.controllers.mpc import MPC
from src.simulation.engine import simulate
from src.simulation.metrics import overshoot, settling_time

# -----------------------------
# System (linear model)
# -----------------------------
A = np.array([[0, 1],
              [-0.5, -0.8]])

B = np.array([[0],
              [1]])

# -----------------------------
# Controller tuning
# -----------------------------
Q = np.diag([80, 15])
R = np.array([[10]])

pid = PID(50, 10, 15)
lqr = LQR(A, B, Q, R)
mpc = MPC(A, B, Q, R, N=10)

# -----------------------------
# Run simulations
# -----------------------------
print("Running PID...")
pid_data = simulate(pid)

print("Running LQR...")
lqr_data = simulate(lqr)

print("Running MPC...")
mpc_data = simulate(mpc)

# -----------------------------
# Plot: State (Pitch Angle)
# -----------------------------
plt.figure(figsize=(10,6))

plt.plot(pid_data[:,0], pid_data[:,1], label="PID")
plt.plot(lqr_data[:,0], lqr_data[:,1], label="LQR")
plt.plot(mpc_data[:,0], mpc_data[:,1], label="MPC")

# Reference
plt.plot(pid_data[:,0], pid_data[:,4], '--', label="Reference")

plt.xlabel("Time (s)")
plt.ylabel("Pitch Angle (θ)")
plt.title("Flight Control Comparison")
plt.legend()
plt.grid()

plt.savefig("results/plots/state_comparison.png", dpi=300)
plt.show()

# -----------------------------
# Plot: Control Input
# -----------------------------
plt.figure(figsize=(10,6))

plt.plot(pid_data[:,0], pid_data[:,3], label="PID Control")
plt.plot(lqr_data[:,0], lqr_data[:,3], label="LQR Control")
plt.plot(mpc_data[:,0], mpc_data[:,3], label="MPC Control")

plt.xlabel("Time (s)")
plt.ylabel("Control Input (u)")
plt.title("Control Effort Comparison")
plt.legend()
plt.grid()

plt.savefig("results/plots/control_comparison.png", dpi=300)
plt.show()

# -----------------------------
# Performance Metrics
# -----------------------------
print("\n--- PERFORMANCE METRICS ---")

print("PID Overshoot:", overshoot(pid_data[:,1]))
print("LQR Overshoot:", overshoot(lqr_data[:,1]))
print("MPC Overshoot:", overshoot(mpc_data[:,1]))

print("PID Settling Time:", settling_time(pid_data[:,1]))
print("LQR Settling Time:", settling_time(lqr_data[:,1]))
print("MPC Settling Time:", settling_time(mpc_data[:,1]))
# -----------------------------
# Plot: Control Input
# -----------------------------
plt.figure(figsize=(10,6))

plt.plot(pid_data[:,0], pid_data[:,3], label="PID Control")
plt.plot(lqr_data[:,0], lqr_data[:,3], label="LQR Control")
plt.plot(mpc_data[:,0], mpc_data[:,3], label="MPC Control")

plt.xlabel("Time (s)")
plt.ylabel("Control Input (u)")
plt.title("Control Effort Comparison")
plt.legend()
plt.grid()

# save file
plt.savefig("results/plots/control_comparison.png", dpi=300)

plt.show()