# import os
# os.getcwd()

#If you type a line of code update the repo

import pandas as pd
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt

# importing data 
df = pd.read_csv('Data.xlsx', delimiter=',', header = 0)
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
        


 #for the heat graph

#Loading in our data set
yssrb_data= pd.read_csv('')
#Question Number that we add
yssrb_data("Question Number")=


#Creating the heat map image 
fig = plt.figure(figsize=(12,12))
r = sns.heatmap(flight_matrox, cmap='BuPu')
r.set_titles("Coorelation of YRBSS Data 2023")

