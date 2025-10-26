import matplotlib.pyplot as plt
import numpy as np



if __name__ == "__main__":


    # Direction vector and point
    P0 = np.array([1, 2, 3])
    d = np.array([4, -1, 2])

    # Parameter t values
    t = np.linspace(-1, 1, 10)

    # Line points
    x = P0[0] + d[0]*t
    y = P0[1] + d[1]*t
    z = P0[2] + d[2]*t

    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label='Line in 3D', marker='o')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.legend()
    plt.show()
