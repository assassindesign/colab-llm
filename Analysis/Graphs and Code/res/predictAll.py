import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataset_sizes = [5000, 15000, 30000, 45000, 60000, 75000, 90000, 100000]
accuracies = [82.85, 91.95, 94.81, 95.93, 96.57, 96.64, 96.71, 96.85]
grammar = [94.50, 94.79, 95.50, 96.43, 97.07, 97.50, 97.86, 98.64]
semantics = [91.50, 92.79, 93.64, 94.14, 94.64, 95.02, 95.71, 97.14]
robustness = [93.86, 94.36, 95.02, 96.83, 97.01, 97.21, 97.23, 97.36]

dataset_sizes = np.array(dataset_sizes).reshape(-1, 1)
accuracies = np.array(accuracies).reshape(-1, 1)
grammar = np.array(grammar).reshape(-1, 1)
semantics = np.array(semantics).reshape(-1, 1)
robustness = np.array(robustness).reshape(-1, 1)

accuracy_model = LinearRegression().fit(dataset_sizes, accuracies)
grammar_model = LinearRegression().fit(dataset_sizes, grammar)
semantics_model = LinearRegression().fit(dataset_sizes, semantics)
robustness_model = LinearRegression().fit(dataset_sizes, robustness)

new_dataset_sizes = np.linspace(0, 1000000, 1000).reshape(-1, 1)

predicted_accuracies = accuracy_model.predict(new_dataset_sizes)
predicted_grammar = grammar_model.predict(new_dataset_sizes)
predicted_semantics = semantics_model.predict(new_dataset_sizes)
predicted_robustness = robustness_model.predict(new_dataset_sizes)

predicted_df = pd.DataFrame({
    'Dataset Sizes': new_dataset_sizes.flatten(),
    'Predicted Accuracy': predicted_accuracies.flatten(),
    'Predicted Grammar': predicted_grammar.flatten(),
    'Predicted Semantics': predicted_semantics.flatten(),
    'Predicted Robustness': predicted_robustness.flatten()
})

plt.plot(dataset_sizes, accuracies, 'o-', label='Accuracy')
plt.plot(dataset_sizes, grammar, 'o-', label='Grammar')
plt.plot(dataset_sizes, semantics, 'o-', label='Semantics')
plt.plot(dataset_sizes, robustness, 'o-', label='Robustness')
plt.plot(predicted_df['Dataset Sizes'], predicted_df['Predicted Accuracy'], '--', label='Predicted Accuracy')
plt.plot(predicted_df['Dataset Sizes'], predicted_df['Predicted Grammar'], '--', label='Predicted Grammar')
plt.plot(predicted_df['Dataset Sizes'], predicted_df['Predicted Semantics'], '--', label='Predicted Semantics')
plt.plot(predicted_df['Dataset Sizes'], predicted_df['Predicted Robustness'], '--', label='Predicted Robustness')

plt.xlabel('Dataset Size')
plt.ylabel('Performance')
plt.title('Dataset Size vs Performance Metrics')
plt.legend()
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

dataset_sizes = [5000, 15000, 30000, 45000, 60000, 75000, 90000, 100000]
accuracies = [82.85, 91.95, 94.81, 95.93, 96.57, 96.64, 96.71, 96.85]

coefficients = np.polyfit(dataset_sizes, accuracies, 1)
polynomial = np.poly1d(coefficients)

x_trend = np.arange(5000, 1000000, 100000)
y_trend = polynomial(x_trend)
plt.scatter(dataset_sizes, accuracies, label="Data Points")
plt.plot(x_trend, y_trend, label="Trend Line")
plt.xlabel("Dataset Size")
plt.ylabel("Accuracy")
plt.title("Dataset Size vs. Accuracy Trend")
plt.legend()
plt.savefig("dataset_size_vs_accuracy_trend.png")
plt.show()

