import matplotlib.pyplot as plt

dataset_sizes = [5000, 15000, 30000, 45000, 60000, 75000, 90000, 100000]
robustness = [93.86,94.36,95.02,96.83,97.01,97.21,97.23,97.36]

plt.plot(dataset_sizes, robustness, marker='o',color='cyan')
plt.xlabel('Dataset Size (rows)')
plt.ylabel('Robustness (%)')
plt.title('Robustness vs. Dataset Size')
plt.grid(True)
plt.xticks(dataset_sizes, rotation=45)
plt.savefig("Robustness_VS_Dataset_Size.png")
plt.show()
