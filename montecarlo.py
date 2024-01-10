import random
import matplotlib.pyplot as plt

def estimate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance = x**2 + y**2

        if distance <= 1:
            inside_circle += 1

    return (inside_circle / num_points) * 4

def plot_points(points_inside):
    plt.scatter(points_inside[0], points_inside[1], color='blue', marker='.')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Monte Carlo Simulation for π Estimation')
    plt.axis('equal')  # Set equal scaling for x and y axes to visualize the circle
    plt.show()

def main():
    num_points = int(input("Enter the number of points: "))

    points_inside = [[], []]
    points_outside = [[], []]

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance = x**2 + y**2

        if distance <= 1:
            points_inside[0].append(x)
            points_inside[1].append(y)
        else:
            points_outside[0].append(x)
            points_outside[1].append(y)

    pi_estimate = estimate_pi(num_points)
    print(f"\nEstimation of π using {num_points} points: {pi_estimate}")

    plot_points(points_inside)

if __name__ == "__main__":
    main()
