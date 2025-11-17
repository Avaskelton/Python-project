import pandas as pd
import numpy as np

# importing data 
df = pd.read_csv('Yssrb_data.txt', delimiter=',', header = 0)
df.head()
# converting any string types into numeric values
df = df.apply(pd.to_numeric, errors='coerce')

corr = df.corr()
print(corr)

# looping throrugh every pair of columns to check if they correlate
for col1 in corr.columns:
    for col2 in corr.columns:
        if col1 == col2:
            continue # skips self  correlations
        value = corr.loc[col1, col2]
        # checking for strong correlations
        if abs(value) > 0.5:
            print(f'{col1} and {col2}: STRONG correlation ({value: .2f})')
        # checking for weak correlations
        else:
            print(f'{col1} and {col2}: WEAK correlation ({value: .2f})')
        


 #for the heat graph

#Seaborn code
import seaborn as sns
fig = plt.figure(figsize=(12,12))
r = sns.heatmap(flight_matrox, cmap='BuPu')
r.set_titles("Coorelation of YRBSS Data 2023")

