import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load datasets, skipping the first row if it contains headers
train_data = pd.read_csv("train.csv", header=None, skiprows=1)
test_data = pd.read_csv("test.csv", header=None, skiprows=1)

# Convert data to numeric values
X_train, y_train = train_data[0].astype(float).values, train_data[1].astype(float).values
X_test, y_test = test_data[0].astype(float).values, test_data[1].astype(float).values

# Store SSE values
sse_train = []
sse_test = []

# Plot polynomial fits
plt.figure(figsize=(12, 10))
for degree in range(8):
    # Fit polynomial model
    coeffs = np.polyfit(X_train, y_train, degree)
    poly = np.poly1d(coeffs)

    # Predict values
    y_train_pred = poly(X_train)
    y_test_pred = poly(X_test)

    # Compute SSE
    sse_train.append(np.sum((y_train - y_train_pred) ** 2))
    sse_test.append(np.sum((y_test - y_test_pred) ** 2))

    # Plot training data and model
    plt.subplot(4, 2, degree + 1)
    plt.scatter(X_train, y_train, color='blue', label='Training Data')
    x_range = np.linspace(min(X_train), max(X_train), 100)
    plt.plot(x_range, poly(x_range), color='red', label=f'Polynomial (Degree {degree})')
    plt.xlabel("x")
    plt.ylabel("r")
    plt.legend()
    plt.title(f"Polynomial Fit (Degree {degree})")
plt.tight_layout()
plt.show()

# Plot SSE values
plt.figure(figsize=(8, 5))
plt.plot(range(8), sse_train, marker='o', linestyle='-', label='Train SSE')
plt.plot(range(8), sse_test, marker='s', linestyle='--', label='Test SSE')
plt.xlabel("Polynomial Degree")
plt.ylabel("Sum of Squared Errors (SSE)")
plt.legend()
plt.title("SSE vs Polynomial Degree")
plt.show()