import numpy as np
import matplotlib.pyplot as plt

dataset_sizes = [5000, 15000, 30000, 45000, 60000, 75000, 90000, 100000]
accuracies = [82.85, 91.95, 94.81, 95.93, 96.57, 96.64, 96.71, 96.85]
coeffs = np.polyfit(dataset_sizes, accuracies, 1)
line_of_best_fit = np.polyval(coeffs, dataset_sizes)

extrapolated_dataset_sizes = np.arange(100000, 200000, 10000)
extrapolated_accuracies = np.polyval(coeffs, extrapolated_dataset_sizes)

plt.plot(dataset_sizes, accuracies, marker='o', label='Data Points')
plt.plot(dataset_sizes, line_of_best_fit, label='Line of Best Fit')
plt.plot(extrapolated_dataset_sizes, extrapolated_accuracies, '--', label='Extrapolated Line')
plt.xlabel('Dataset Size')
plt.ylabel('Accuracy')
plt.title('Dataset Size vs. Accuracy')
plt.grid(True)
plt.legend()
plt.show()
