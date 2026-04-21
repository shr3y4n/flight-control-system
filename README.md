Flight Control System Simulation (PID vs LQR vs MPC)

## 🎯 Controller Comparison at a Glance

| Controller | Behavior |
|----------|--------|
| PID | Fast but aggressive, high control spikes |
| LQR | Smooth optimal response |
| MPC | Predictive, smoothest control effort |

### ✈️ Overview

This project simulates aircraft pitch control using three control strategies:
PID, LQR, and MPC.

It demonstrates how modern control methods outperform classical approaches in terms of stability, efficiency, and predictive capability under disturbances.

This project implements and compares three fundamental control strategies used in aerospace systems:

PID Control (Classical)
LQR (Optimal Control)
MPC (Predictive Control)

The system simulates aircraft pitch dynamics under disturbances and evaluates controller performance in terms of stability, tracking, and control effort.
## Features
Nonlinear/linear aircraft pitch model
Step reference tracking
Wind disturbance + noise
PID, LQR, and MPC controllers
## Performance metrics:
Overshoot
Settling time
Control input comparison
 Results
State Response

Control Effort

## 🧪 Simulation Details

- System: Aircraft pitch dynamics (2-state model)
- Disturbances: Wind + measurement noise
- Controllers:
  - PID (tuned manually)
  - LQR (optimal state feedback)
  - MPC (finite-horizon predictive control)

## Key Insights
PID is simple but oscillatory
LQR provides smooth optimal control
MPC enables predictive control and constraint handling

## 🔍 Key Observations

- PID shows large initial control effort and oscillations  
- LQR provides smooth optimal control  
- MPC achieves predictive tracking with minimal control variation  

This highlights the evolution from reactive → optimal → predictive control systems.

## 🌍 Why This Matters

Modern aerospace systems rely on advanced control strategies like LQR and MPC for stability, efficiency, and robustness under disturbances.

This project demonstrates how predictive control methods can outperform classical techniques in real-world scenarios.

## ⚙️ Installation
git clone https://github.com/shr3y4n/Flight-Control-System.git
cd Flight-Control-System
pip install -r requirements.txt
 Run
python main.py
📁 Project Structure
src/
controllers/ → PID, LQR, MPC
models/ → system dynamics
simulation/ → engine + metrics
disturbances/ → wind + noise
# Future Work
Add constraints to MPC
Implement Kalman Filter
Extend to nonlinear aircraft model
Real-time simulation


## 👨‍💻 Author

## Shreyan Dey
