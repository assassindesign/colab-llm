import matplotlib.pyplot as plt
dataset_sizes = [5000, 15000, 30000, 45000, 60000, 75000, 90000, 100000]
semantics_scores = [91.50, 92.79, 93.64, 94.14, 94.64, 95.02, 95.71, 97.14]

plt.plot(dataset_sizes, semantics_scores, marker='o', color='purple')
plt.xlabel('Dataset Size (rows)')
plt.ylabel('Semantics Score (%)')
plt.title('Semantics vs. Dataset Size')
plt.grid(True)
plt.xticks(dataset_sizes, rotation=45)
plt.savefig("Semantics_VS_Datsset_Size.png")
plt.show()
