import matplotlib.pyplot as plt

dataset_sizes = [5000, 15000, 30000, 45000, 60000, 75000, 90000, 100000]
accuracies = [82.85, 91.95, 94.81, 95.93, 96.57, 96.64, 96.71, 96.85]

plt.plot(dataset_sizes, accuracies, marker='o',color='green')
plt.xlabel('Dataset Size (rows)')
plt.ylabel('Accuracy (%)')
plt.title('Accuracy vs. Dataset Size')
plt.grid(True)
plt.xticks(dataset_sizes, rotation=45)
plt.savefig("Accuracy_VS_Datsset_Size.png")
plt.show()
