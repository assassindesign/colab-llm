import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

dataset_sizes = np.array([5000, 15000, 30000, 45000, 60000, 75000, 90000, 100000])
training_cost = np.array([1.46,1.54,2.40,2.44,3.45,3.51,3.54,3.62])

# Convert training cost to dollars
compute_units_to_dollars = 11 / 100
training_cost_dollars = training_cost * compute_units_to_dollars

# Fit a linear regression model
regression_model = LinearRegression()
regression_model.fit(dataset_sizes.reshape(-1, 1), training_cost_dollars)

# Generate predicted values for larger dataset sizes
x_predicted = np.arange(5000, 200000, 1000)
y_predicted_dollars = regression_model.predict(x_predicted.reshape(-1, 1))

# Convert predicted values back to compute units
y_predicted_compute_units = y_predicted_dollars / compute_units_to_dollars

# Set any negative predicted values to zero
y_predicted_compute_units[y_predicted_compute_units < 0] = 0

# Plot the dataset_sizes vs. training_cost
plt.plot(dataset_sizes, training_cost, marker='o', label='Original Data')
plt.plot(x_predicted, y_predicted_compute_units, '--', label='Extrapolated Trend')

# Add labels and title
plt.xlabel("Dataset Size (No. of Rows)")
plt.ylabel("Training Cost (Compute Units)")
plt.title("Dataset Size vs. Training Cost")

# Show legend
plt.legend()

# Show the plot
plt.show()
