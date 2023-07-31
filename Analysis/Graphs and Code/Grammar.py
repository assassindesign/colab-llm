import matplotlib.pyplot as plt
dataset_sizes = [5000, 15000, 30000, 45000, 60000, 75000, 90000, 100000]
grammar_scores = [94.50, 94.79, 95.50, 96.43, 97.07, 97.50, 97.86, 98.64]

plt.plot(dataset_sizes, grammar_scores, marker='o', color='blue')
plt.xlabel('Dataset Size (rows)')
plt.ylabel('Grammar Score (%)')
plt.title('Grammar vs. Dataset Size')
plt.grid(True)
plt.xticks(dataset_sizes, rotation=45)
plt.savefig("Grammar_VS_Dataset_Size.png")
plt.show()

