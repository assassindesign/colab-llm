import matplotlib.pyplot as plt

dataset_sizes = [5000, 15000, 30000, 45000, 60000, 75000, 90000, 100000]
time_Fine_Tuning = [16.09, 17.01, 26.87, 26.44, 39.05, 38.71, 39.01, 38.87]

plt.plot(dataset_sizes, time_Fine_Tuning, marker='o', color='red')
plt.xlabel('Dataset Size (rows)')
plt.ylabel('Fine Tuning Time (mins)')
plt.title('Time vs. Dataset Size')
plt.grid(True)
plt.xticks(dataset_sizes, rotation=45)
plt.savefig("Time_VS_Dataset_Size.png")
plt.show()


