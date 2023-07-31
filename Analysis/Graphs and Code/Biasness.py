import matplotlib.pyplot as plt

dataset_sizes = [5000, 15000, 30000, 45000, 60000, 75000, 90000, 100000]
bias_scores = [93.00, 93.57, 94.36, 95.07, 95.64, 96.48 ,97.00, 98.36]

plt.plot(dataset_sizes, bias_scores, marker='o', color='orange')
plt.xlabel('Dataset Size (rows)')
plt.ylabel('Bias Score (%)')
plt.title('Bias vs. Dataset Size')
plt.grid(True)
plt.xticks(dataset_sizes, rotation=45)
plt.savefig("Biasness_VS_Dataset_Size.png")
plt.show()
