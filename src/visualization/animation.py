import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

def rotate(points, theta):
    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    return points @ R.T


def animate_pitch(data):
    os.makedirs("results/plots", exist_ok=True)

    fig, ax = plt.subplots(figsize=(5,5))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_title("Aircraft Pitch Animation")

    # ✈️ aircraft shape (relative coordinates)
    body = np.array([
        [0, 0.3],
        [0, -0.3]
    ])

    wings = np.array([
        [-0.4, 0],
        [0.4, 0]
    ])

    tail = np.array([
        [-0.2, -0.25],
        [0.2, -0.25]
    ])

    body_line, = ax.plot([], [], 'b-', lw=3)
    wing_line, = ax.plot([], [], 'r-', lw=2)
    tail_line, = ax.plot([], [], 'g-', lw=2)

    def update(frame):
        theta = data[frame, 1]

        # rotate all parts
        body_r = rotate(body, theta)
        wings_r = rotate(wings, theta)
        tail_r = rotate(tail, theta)

        # update plots
        body_line.set_data(body_r[:,0], body_r[:,1])
        wing_line.set_data(wings_r[:,0], wings_r[:,1])
        tail_line.set_data(tail_r[:,0], tail_r[:,1])

        return body_line, wing_line, tail_line

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(data),
        interval=20,
        blit=True
    )

    gif_path = os.path.abspath("results/plots/animation.gif")
    print("Saving animation to:", gif_path)

    ani.save(gif_path, writer="pillow", fps=30)

    print("Aircraft animation saved!")

    plt.close(fig)