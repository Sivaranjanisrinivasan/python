import matplotlib.pyplot as plt
import numpy as np



data = [12, 15, 14, 10, 18, 20, 22, 15, 17, 19, 16, 14, 13, 15, 18]


plt.figure(figsize=(10, 4))
plt.scatter(range(len(data)), data)
plt.title('Scatter Plot of Data')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()


heat_data = np.array(data).reshape(5, 3)

plt.figure(figsize=(6, 5))
plt.imshow(heat_data)
plt.colorbar()
plt.title('Heat Map of Data')
plt.show()
