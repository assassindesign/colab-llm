# import matplotlib.pyplot as plt
# import numpy as np
# from sklearn.linear_model import LinearRegression

# dataset_sizes = np.array([5000, 15000, 30000, 45000, 60000, 75000, 90000, 100000])
# time_Fine_Tuning = np.array([16.09, 17.01, 26.87, 26.44, 39.05, 38.71, 39.01, 38.87])

# # Fit a linear regression model
# regression_model = LinearRegression()
# regression_model.fit(dataset_sizes.reshape(-1, 1), time_Fine_Tuning)

# # Generate predicted values for larger dataset sizes
# x_predicted = np.arange(5000, 100001, 1000)
# y_predicted = regression_model.predict(x_predicted.reshape(-1, 1))

# # Plot the dataset_sizes vs. time_Fine_Tuning
# plt.plot(dataset_sizes, time_Fine_Tuning, marker='o', label='Original Data')
# plt.plot(x_predicted, y_predicted, '--', label='Extrapolated Trend')

# # Add labels and title
# plt.xlabel("Dataset Size (No. of Rows)")
# plt.ylabel("Time for Fine Tuning (minutes)")
# plt.title("Dataset Size vs. Time for Fine Tuning")

# # Show legend
# plt.legend()

# # Show the plot
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

dataset_sizes = np.array([5000, 15000, 30000, 45000, 60000, 75000, 90000, 100000])
time_Fine_Tuning = np.array([16.09, 17.01, 26.44, 26.87, 38.05, 38.71, 39.01, 39.87])

regression_model = LinearRegression()
regression_model.fit(dataset_sizes.reshape(-1, 1), time_Fine_Tuning)

x_predicted = np.arange(5000, 200000, 1000)
y_predicted = regression_model.predict(x_predicted.reshape(-1, 1))

plt.plot(dataset_sizes, time_Fine_Tuning, marker='o', label='Original Data')
plt.plot(x_predicted, y_predicted, '--', label='Extrapolated Trend')

plt.xlabel("Dataset Size (No. of Rows)")
plt.ylabel("Time for Fine Tuning (minutes)")
plt.title("Dataset Size vs. Time for Fine Tuning")
plt.grid(True)
plt.legend()
plt.savefig("Prediction_Time.png")
plt.show()
