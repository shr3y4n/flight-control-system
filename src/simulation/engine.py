import numpy as np
from src.models.nonlinear import dynamics
from src.disturbances.wind import wind
from src.disturbances.noise import noise

def simulate(controller, estimator=None):
    dt = 0.01
    T = 15
    steps = int(T / dt)

    x = np.array([0.2, 0])   # initial disturbance
    history = []

    for i in range(steps):
        t = i * dt

        # 🔥 STEP INPUT (reference tracking)
        ref = 0.2 if t > 2 else 0

        # noisy measurement
        measured = x[0] + noise()

        # state estimation (if using Kalman later)
        if estimator:
            estimator.predict(0)
            estimator.update(np.array([[measured]]))
            x_used = estimator.x.flatten()
        else:
            x_used = x

        # controller input
        u = controller.compute(x_used, ref, dt)

        # safety: ensure scalar
        u = float(u)

        # actuator saturation
        u = np.clip(u, -15, 15)

        # system dynamics with disturbance
        dx = dynamics(x, u + wind(t))
        x = x + dx * dt

        history.append([t, x[0], x[1], u, ref])

    return np.array(history)