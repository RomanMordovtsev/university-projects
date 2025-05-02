import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data(filename):
    """Load data from CSV file"""
    data = pd.read_csv(filename)
    return data.values


def initialize_centroids(data, k):
    """Randomly initialize k centroids"""
    indices = np.random.choice(len(data), k, replace=False)
    return data[indices]


def assign_clusters(data, centroids):
    """Assign each data point to the nearest centroid"""
    distances = np.sqrt(((data[:, np.newaxis] - centroids) ** 2).sum(axis=2))
    return np.argmin(distances, axis=1)


def update_centroids(data, assignments, k):
    """Update centroids as the mean of assigned points"""
    new_centroids = np.zeros((k, data.shape[1]))
    for i in range(k):
        cluster_points = data[assignments == i]
        if len(cluster_points) > 0:
            new_centroids[i] = cluster_points.mean(axis=0)
    return new_centroids


def calculate_loss(data, centroids, assignments):
    """Calculate reconstruction loss (sum of squared distances)"""
    loss = 0
    for i, centroid in enumerate(centroids):
        cluster_points = data[assignments == i]
        if len(cluster_points) > 0:
            loss += np.sum((cluster_points - centroid) ** 2)
    return loss


def kmeans(data, k, max_iter=100, tol=1e-4):
    """Run k-means algorithm"""
    best_centroids = None
    best_assignments = None
    best_loss = float('inf')

    for _ in range(10):  # Run 10 times as per requirements
        centroids = initialize_centroids(data, k)
        prev_loss = float('inf')

        for _ in range(max_iter):
            assignments = assign_clusters(data, centroids)
            centroids = update_centroids(data, assignments, k)
            current_loss = calculate_loss(data, centroids, assignments)

            if np.abs(prev_loss - current_loss) < tol:
                break
            prev_loss = current_loss

        if current_loss < best_loss:
            best_loss = current_loss
            best_centroids = centroids
            best_assignments = assignments

    return best_centroids, best_assignments, best_loss


def plot_loss(loss_values):
    """Plot mean reconstruction loss for each k"""
    plt.figure(figsize=(10, 6))
    k_values = list(loss_values.keys())
    mean_loss = [np.mean(loss_values[k]) for k in k_values]
    std_loss = [np.std(loss_values[k]) for k in k_values]

    plt.errorbar(k_values, mean_loss, yerr=std_loss, fmt='-o', capsize=5)
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Mean Reconstruction Loss')
    plt.title('Mean Reconstruction Loss vs. Number of Clusters')
    plt.grid(True)
    plt.savefig('loss_plot.png')
    plt.show()


def plot_clusters(data, assignments, centroids, k):
    """Plot clustering visualization"""
    plt.figure(figsize=(10, 6))
    colors = ['r', 'g', 'b', 'c', 'm', 'y']
    markers = ['o', 's', '^', 'D', 'v', 'p']

    for i in range(k):
        cluster_points = data[assignments == i]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1],
                    c=colors[i], marker=markers[i], label=f'Cluster {i + 1}')

    plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='k', marker='*', label='Centroids')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title(f'K-Means Clustering (k={k})')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'clusters_k_{k}.png')
    plt.show()


def main():
    # Load data
    data = load_data('data.csv')

    # Run k-means for k=1 to 6
    k_values = range(1, 7)
    loss_values = {k: [] for k in k_values}
    best_results = {}

    for k in k_values:
        print(f"Running k-means for k={k}...")
        for trial in range(10):
            centroids, assignments, loss = kmeans(data, k)
            loss_values[k].append(loss)

        # Get the best result (minimum loss) for this k
        best_trial = np.argmin(loss_values[k])
        centroids, assignments, _ = kmeans(data, k)
        best_results[k] = (centroids, assignments)

    # Plot mean reconstruction loss
    plot_loss(loss_values)

    # Plot clustering visualizations for best trials
    for k in k_values:
        centroids, assignments = best_results[k]
        plot_clusters(data, assignments, centroids, k)


if __name__ == "__main__":
    main()