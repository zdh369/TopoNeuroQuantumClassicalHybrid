import numpy as np
import matplotlib.pyplot as plt

def poincare_section(trajectory, plane_index=0, plane_value=0.0, direction=1):
    """
    Compute Poincaré section of a trajectory crossing a plane.
    trajectory: np.ndarray of shape (time_steps, dim)
    plane_index: index of coordinate defining the plane
    plane_value: value of the plane coordinate
    direction: +1 for increasing crossing, -1 for decreasing crossing
    Returns points on the section.
    """
    points = []
    for i in range(1, len(trajectory)):
        prev = trajectory[i-1, plane_index]
        curr = trajectory[i, plane_index]
        if direction > 0 and prev < plane_value <= curr:
            points.append(trajectory[i])
        elif direction < 0 and prev > plane_value >= curr:
            points.append(trajectory[i])
    return np.array(points)

def fractal_dimension(points, min_box_size=0.01, max_box_size=1.0, num_sizes=10):
    """
    Estimate fractal dimension using box-counting method.
    points: np.ndarray of shape (num_points, dim)
    """
    sizes = np.logspace(np.log10(min_box_size), np.log10(max_box_size), num_sizes)
    counts = []
    for size in sizes:
        bins = [np.arange(np.min(points[:,i]), np.max(points[:,i]) + size, size) for i in range(points.shape[1])]
        hist, _ = np.histogramdd(points, bins=bins)
        counts.append(np.sum(hist > 0))
    coeffs = np.polyfit(np.log(sizes), np.log(counts), 1)
    return -coeffs[0]

def plot_poincare_section(points):
    if points.shape[1] < 2:
        raise ValueError("Need at least 2D points to plot Poincaré section")
    plt.scatter(points[:,1], points[:,2], s=1)
    plt.title("Poincaré Section")
    plt.xlabel("Coordinate 1")
    plt.ylabel("Coordinate 2")
    plt.show()

if __name__ == "__main__":
    # Example usage with Lorenz attractor trajectory loaded externally
    # trajectory = load_trajectory()  # shape (time_steps, 3)
    # For demonstration, generate dummy data
    t = np.linspace(0, 50, 10000)
    trajectory = np.column_stack((np.sin(t), np.cos(t), np.sin(2*t)))

    section = poincare_section(trajectory, plane_index=0, plane_value=0.0, direction=1)
    print(f"Poincaré section points: {section.shape[0]}")

    fd = fractal_dimension(section)
    print(f"Estimated fractal dimension: {fd:.4f}")

    plot_poincare_section(section)
