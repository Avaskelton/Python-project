import pandas as pd
<<<<<<< HEAD
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# importing data 
df = pd.read_csv('Yssrb_data_new.txt', delimiter=',', header = 0)
=======
import numpy as np
import matplotlib.pyplot as plt
#loading data
# clean_lines = []
# with open('Yssrb_data.txt', 'r') as f:
#     for line in f:
#         clean_line = line.replace(',', '')  # remove commas
#         clean_lines.append(clean_line)

# # Optionally save cleaned data
# with open('Yssrb_data_clean.txt', 'w') as f:
#     f.writelines(clean_lines)
df = pd.read_csv('Yssrb_data.txt', delimiter=',', header = 0)
>>>>>>> 2f0ea7364ad5fd947078ffd5a255b703e34cc72b
df.head()




print(df.head())

<<<<<<< HEAD
#Seaborn code
# Create a random 10x10 matrix
data = np.random.rand(10, 10)

# Create the heatmap
plt.figure(figsize=(8, 6))
plt.imshow(data, cmap="viridis", interpolation="nearest")
plt.colorbar(label="Intensity")
plt.title("Heatmap Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
=======
#df = df.replace(',', '', regex=True)
# for line in df:
#     parts = line.strip().split(',')

>>>>>>> 2f0ea7364ad5fd947078ffd5a255b703e34cc72b
