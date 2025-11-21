# import os
# os.getcwd()

#<<<<<<< HEAD 

# import tkinter as tk
#=======
#If you type a line of code update the repo

#>>>>>>> a7ae807dbd510c171b3dfe0ea6e8df3467b08479
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# importing data 
df = pd.read_csv('Yssrb_data_new.txt', delimiter=',', header = 0)
df.head()
# converting any string types into numeric values
df = df.apply(pd.to_numeric, errors='coerce')

corr = df.corr()
print(corr)

# looping throrugh every pair of columns to check if they correlate
for i, col1 in enumerate(corr.columns):
    for j, col2 in enumerate(corr.columns):
        if j <= i:
            continue # skips self  correlations
        value = corr.iloc[i, j]
        # Organizing correlations
        if abs(value) > 0.8:
            print(f'{col1} and {col2}: VERY STRONG correlation ({value: .2f})')
        elif abs(value) > 0.5:
           print(f'{col1} and {col2}: STRONG correlation ({value: .2f})') 
        elif abs(value) > 0.3:
            print(f'{col1} and {col2}: MODERATE correlation ({value: .2f})')
        else:
            print(f'{col1} and {col2}: WEAK correlation ({value: .2f})')
        
#<<<<<<< HEAD


root = tk.Tk()
root.title("Tk Example")
root.configure(background="yellow")
root.minsize(200,200)
root.maxsize(500,500)
root.geometry("300x300+50+50")
root.mainloop()
 
#=======


 #for the heat graph

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
