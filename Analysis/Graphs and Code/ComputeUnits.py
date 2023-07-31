import matplotlib.pyplot as plt
dataset_sizes = [5000, 15000, 30000, 45000, 60000, 75000, 90000, 100000]
training_cost=[1.46,1.54,2.40,2.44,3.45,3.51,3.54,3.62]
plt.plot(dataset_sizes, training_cost, marker='o', color='red')
plt.xlabel('Dataset Size (rows)')
plt.ylabel('Compute units ')
plt.title('Compute Units vs. Dataset Size')
plt.xticks(dataset_sizes, rotation=45)
plt.grid(True)
plt.savefig("Compute_Units_VS_Dataset_Size.png")
plt.show()